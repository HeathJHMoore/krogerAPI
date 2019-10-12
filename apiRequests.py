import variables as v
import requests

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

# This function loops through each location and product to gather a product's price and name
def getProductInfo(accessToken):
  productInfoList = []
  for location in v.locationIds:
    for product in v.productIds:
      response = makeProductRequest(location, product, accessToken).json()
      productDailyPrice = {
        'productId' : product,
        'locationId' : location,
        'productName' : response['data']['description'],
        'productRegularPrice' : response['data']['items'][0]['price']['regular'],
        'productPromoPrice' : response['data']['items'][0]['price']['promo']
      }
      productInfoList.append(productDailyPrice)
  return productInfoList