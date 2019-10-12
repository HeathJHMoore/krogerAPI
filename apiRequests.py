import variables as v
import requests

def makeTokenRequest():
  request = requests.post(
  v.API_Token_Endpoint,
  headers={
    'Authorization' : v.client_credentials,
    'Content-Type' : 'application/x-www-form-urlencoded'
  },
  data={
    'grant_type' : 'client_credentials',
    'scope' : 'product.compact'
  }
  )
  return request

def makeProductRequest(locationId, productId, accessToken):
  productRequest = requests.get(
  f'{v.API_Product_Endpoint}/{productId}?filter.locationId={locationId}',
  headers={
    'Authorization' : f'Bearer {accessToken}',
    'Content-Type': 'application/json'
  }
  )
  return productRequest

def getProductInfo(accessToken):
  productInfoList = []
  for location in v.locationIds:
    for product in v.productIds:
      response = makeProductRequest(location, product, accessToken).json()
      print(response['data']['items'][0]['price'])
      # productInfoList.append(listItem)
  return productInfoList