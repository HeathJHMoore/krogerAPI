# Kroger API

This is a python script that I am using to collect product pricing data daily from Kroger's public API. Currently, I am tracking about 80 different products at 9 different Kroger locations around Nashville. I am hoping to determine if Kroger predictably runs promo's or clearances on certain items by visualizing the price action of this data from a daily, weekly, and monthly perspective.

# How it works
For this project, I have set up a PostgreSQL database on Heroku to capture my daily product information. I am using OAuth2 to gain access to Kroger's API so that I can make GET requests to their Product API. After collecting product data with a GET request, I programatically create a large SQL Insert statement that gets inserted to my Heroku PostgreSQL database. After the SQL Insert statements occurs, an automated email is sent to my personal gmail to let me know how many rows were inserted that night as well as how many of the products are on promotion that day. Over the next two months, I plan to build out a Web based interface that utilizes a C#/.NET backend API to access my PostgreSQL database 

