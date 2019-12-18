# import mysql.connector
import psycopg2
import variables as v

# establish connection to mysql kroger database
def openDatabaseConnection():
  mydb = psycopg2.connect("dbname=dejbdamcql57c9 host=ec2-107-21-98-89.compute-1.amazonaws.com user=ayhcbbfncdbyqq password=630b33bc63bf86e30540c5e9b359e48d8c00274a46b8f21a0be0dad11af0545b")
  return mydb


# THIS FUNCTION CREATES A DATABASE CONNECTION IN MYSQL
# def establishDatabaseConnection():
#   mydb = mysql.connector.connect(
#     host="heathjhmoore.mysql.pythonanywhere-services.com",
#     user=v.mySQLUsername,
#     passwd=v.mySQLPassword
#   )
#   return mydb

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
    # valueString += f'"{productId}", "{locationId}", "{productName}", {productRegularPrice}, {productPromoPrice}, "{captureDate}"'
    valueString += f"'{productId}', '{locationId}', '{productName}', {productRegularPrice}, {productPromoPrice}, '{captureDate}'"
    valueString += ')'
    # the below f string has syntax problems that I cannot figure out so I resorted to the above methodology
    # valueString += f'({product['productId']}, {product['locationId']}, {product['productName']}, {product['productRegularPrice']}, {product['productPromoPrice']}, {product['captureDate']})'
    if productList.index(product) != len(productList) - 1:
      valueString += ', '
  return valueString

# execute SQL insert statement to insert product information into daily_product_snapshot table
def insertValues(productList):
  database = openDatabaseConnection()
  values = createValueStatements(productList)
  databaseCursor = database.cursor()
  sql = f'INSERT INTO daily_product_snapshot (productId, locationId, productName, productRegularPrice, productPromoPrice, captureDate) {values};'
  databaseCursor.execute(sql)
  database.commit()
  databaseCursor.close()
  database.close()




# THIS IS HOW TO INSERT VALUES IN MYSQL
# def insertValues(productList):
#   database = establishDatabaseConnection()
#   values = createValueStatements(productList)
#   databaseCursor = database.cursor()
#   sql = f'INSERT INTO heathjhmoore$krogerdata.daily_product_snapshot {values};'
#   databaseCursor.execute(sql)
#   database.commit()


