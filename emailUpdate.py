import asyncio
import smtplib 
import ssl
import insertSQL as it
import datetime
import time
import email.message
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



# ---------------Global Variables--------------------------------------

port_number = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "mygrocerydata@gmail.com"  # Enter your address
receiver_email = "heathjhmoore@gmail.com"  # Enter receiver address
password = "mygrocerydata"
capture_date = datetime.datetime.now().strftime('%Y-%m-%d')
total_rows = None
promo_rows = None
email_file_name = r'./email_message.txt'

# ---------------Global Variables--------------------------------------



# function used to set global variables used in the body of the email message
async def setEmailVariables():
  global total_rows
  global promo_rows
  database = it.openDatabaseConnection()
  databaseCursor = database.cursor()
  total_rows_sql = f"SELECT count(*) FROM daily_product_snapshot WHERE captureDate = '{capture_date}';"
  databaseCursor.execute(total_rows_sql)
  # cursor fetch returns tuples so use indexing to get exact result
  output_total_rows = databaseCursor.fetchone()
  total_rows = output_total_rows[0]
  promo_rows_sql = f"SELECT count(*) FROM daily_product_snapshot WHERE captureDate = '{capture_date}' AND productPromoPrice <> 0;"
  databaseCursor.execute(promo_rows_sql)
  # cursor fetch returns tuples so use indexing to get exact result
  output_promo_rows = databaseCursor.fetchone()
  promo_rows = output_promo_rows[0]
  database.commit()
  databaseCursor.close()
  database.close()


# function used to open text file and use its contents as email message template
def read_template(filename):
  with open(filename, 'r', encoding='utf-8') as template_file:
      template_file_content = template_file.read()
  return Template(template_file_content)


# set up the SMTP server
def SMTP_setup():
  s = smtplib.SMTP('smtp.gmail.com') #port=port_number)
  s.starttls()
  s.login(sender_email, password)
  return s

# main function to gather variables and construct/send email
async def construct_and_send_email():
  await setEmailVariables()
  message_template = read_template(email_file_name)

  # start smtp server to send emails
  s = SMTP_setup()
  
  # create new email mime message
  msg = MIMEMultipart()

  # add in variables to email body
  message = message_template.substitute(CAPTURE_DATE=capture_date, TOTAL_ROWS_INSERTED=total_rows, TOTAL_PROMOTION_PRODUCTS=promo_rows)


  # setup the parameters of the message
  msg['From']=sender_email
  msg['To']=receiver_email
  msg['Subject']=f"Daily Update: {capture_date}"

  # add in the message body
  msg.attach(MIMEText(message, 'plain'))

  # send the message via the server set up earlier.
  s.send_message(msg)
  
  del msg


def emailUpdateMain():
  # gathers the event loop for asynchronous action
  loop = asyncio.get_event_loop()
  loop.run_until_complete(construct_and_send_email())
