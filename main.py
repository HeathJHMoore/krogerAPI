import requests
import apiRequests as a

accessToken = ''

try:
  tokenRequest = a.makeTokenRequest()
  postContent = tokenRequest.json();
  accessToken = postContent['access_token']
  print(accessToken)
except Exception as error:
  print(tokenRequest.status_code)
  print(error)

try:
  productList = a.getProductInfo(accessToken)
except Exception as error:
  print(error)
