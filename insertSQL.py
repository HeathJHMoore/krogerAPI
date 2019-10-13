import mysql.connector
import variables as v

# establish connection to mysql kroger database
def establishDatabaseConnection():
  mydb = mysql.connector.connect(
    host="heathjhmoore.mysql.pythonanywhere-services.com",
    user=v.mySQLUsername,
    passwd=v.mySQLPassword
  )
  return mydb

# create VALUE section for insert statement to daily_product_snapshot table
def createValueStatements(productList):
  valueString = 'VALUES '
  for product in productList:
    productId = product['productId']
    locationId = product['locationId']
    productName = product['productName']
    productRegularPrice = product['productRegularPrice']
    productPromoPrice = product['productPromoPrice']
    captureDate = product['captureDate']
    valueString += '('
    valueString += f'"{productId}", "{locationId}", "{productName}", {productRegularPrice}, {productPromoPrice}, "{captureDate}"'
    valueString += ')'
    # the below f string has syntax problems that I cannot figure out so I resorted to the above methodology
    # valueString += f'({product['productId']}, {product['locationId']}, {product['productName']}, {product['productRegularPrice']}, {product['productPromoPrice']}, {product['captureDate']})'
    if productList.index(product) != len(productList) - 1:
      valueString += ', '
  return valueString

# execute SQL insert statement to insert product information into daily_product_snapshot table
def insertValues(productList):
  database = establishDatabaseConnection()
  values = createValueStatements(productList)
  databaseCursor = database.cursor()
  sql = f'INSERT INTO heathjhmoore$krogerdata.daily_product_snapshot {values};'
  databaseCursor.execute(sql)
  database.commit()


