# Kroger API

This is a python project that I am using to collect product pricing data daily from Kroger's public API. I am hoping to determine if Kroger predictably runs promo's or clearances on certain items by visualizing the price action of this data from a daily, weekly, and monthly perspective.

# How it works
For this project, I have set up a PostgreSQL database on Heroku to capture my daily product information. I am using OAuth2 to gain access to Kroger's API so that I can make GET requests to their Product API. After collecting product data with a GET requests, I programatically create a large SQL Insert statement that gets inserted to my Heroku PostgreSQL database. Over the next two months, I plan to build out a Web based interface that utilizes a C# backend API to the access my PostgreSQL database 

