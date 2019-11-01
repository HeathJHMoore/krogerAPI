import requests
import apiRequests as a
import insertSQL as it
import sys

accessToken = ''
productList = []


# Step 1 : Get Access Token to hit Kroger API endpoints
try:
  tokenRequest = a.makeTokenRequest()
  print(tokenRequest)
  postContent = tokenRequest.json()
  accessToken = postContent['access_token']
except Exception as error:
  print(tokenRequest.status_code)
  print(error)
  sys.stdout.flush()


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


print('script is finished')
