import variables as v
import requests
import datetime

# This function makes a POST request to receive an access token.
# An access token is necessary to hit all Kroger API endpoints
def makeTokenRequest():
  request = requests.post(
    v.API_Token_Endpoint,
    headers={
      # Authorization requires clientId:clientSecret in base 64 encoding
      'Authorization' : v.client_credentials,
      'Content-Type' : 'application/x-www-form-urlencoded'
    },
    data={
      'grant_type' : 'client_credentials',
      'scope' : 'product.compact'
    }
  )
  return request

# This function makes a GET request for a specific product at a specific Kroger location
def makeProductRequest(locationId, productId, accessToken):
  productRequest = requests.get(
    f'{v.API_Product_Endpoint}/{productId}?filter.locationId={locationId}',
    headers={
      'Authorization' : f'Bearer {accessToken}',
      'Content-Type': 'application/json'
    }
  )
  return productRequest

# Function created to remove apostrophes from product names to prevent errors on PostGreSQL insert statements
def removeUnauthorizedCharacters(stringToParse):
  fixedWord = ''
  for character in stringToParse:
    if (character != "'"):
      fixedWord += character
  return fixedWord


# This function loops through each location and product to gather all product info into a list
def getProductInfo(accessToken):
  productInfoList = []
  for location in v.locationIds:
    for product in v.productIds:
      response = makeProductRequest(location, product, accessToken).json()
      productDailyInfo = {
        'productId' : product,
        'locationId' : location,
        'productName' : removeUnauthorizedCharacters(response['data']['description']),
        'productRegularPrice' : response['data']['items'][0]['price']['regular'],
        'productPromoPrice' : response['data']['items'][0]['price']['promo'],
        'captureDate' : datetime.datetime.now().strftime('%Y-%m-%d')
      }
      productInfoList.append(productDailyInfo)
  return productInfoList