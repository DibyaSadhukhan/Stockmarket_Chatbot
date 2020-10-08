#importing python modules
from flask import Flask
from flask import request
from twilio.rest import Client
from marketstack import get_stock_price
import os

app = Flask(__name__)
#setting up twilio apis
TWILIO_ACCOUNT='ACf37a9bd6668270a1eccc9d892531e2ba'
TWILIO_TOKEN='7564c2fb4429643ac0a01cb73d482496'

#ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
#TWILIO_TOKEN=os.environ.get('TWILIO_TOKEN')
#the default free twilio number 
TWILIO_NUMBER='whatsapp:+14155238886'
#fuction to generate and process the user recived msg
def process_msg(msg):
    response=""
    if msg.lower()=='hi':
        response="Hi, welcome to the stockmarket Chatbot "
        response +="Type \"sym:stock_symbol\" to know the latest price of the stock. \nFor example: \n sym:AAPL will give you the current stock price of Apple (AAPL)"
    elif ':' in msg:
        data=msg.split(":")
        stock_symbol = data[1]
        stock_price=get_stock_price(stock_symbol)
        if 'resource_not_found' in stock_price:
            response= "Please check the symbol for your query and try again!"
        else:
            response= "The stock details for the stock is: "
            det=stock_price.split('{')[1].split('}')[0]
            for i in range(0,len(det.split(','))):
                response +="\n"+det.split(',')[i]
    else:
        response="Type 'Hi' to get started"
    return response
client = Client(TWILIO_ACCOUNT,TWILIO_TOKEN)
def send_msg(msg,recipient):
    client.messages.create(
        body= msg,
        from_=TWILIO_NUMBER,
        to=recipient
    )
@app.route("/webhook",methods={"POST"})
def webhook():
    f=request.form
    msg=f['Body']
    sender=f['From']
    response=process_msg(msg)
    send_msg(response,sender)
    return "OK",200