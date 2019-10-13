import requests
import apiRequests as a
import insertSQL as it

accessToken = ''
productList = []


# Step 1 : Get Access Token to hit Kroger API endpoints
try:
  tokenRequest = a.makeTokenRequest()
  postContent = tokenRequest.json()
  accessToken = postContent['access_token']
except Exception as error:
  print(tokenRequest.status_code)
  print(error)


# Step 2 : Get a snapshot of all product information for today
try:
  productList = a.getProductInfo(accessToken)
except Exception as error:
  print(error)


# Step 3 : Insert today's product information into mySQL database
try:
  it.insertValues(productList)
except Exception as error:
  print(error)
