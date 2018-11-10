#! /usr/bin/env python3
from docopt import docopt
from twilio.rest import Client
"""REMAINDERS
Usage:
    remainder m "Insert Message"
    remainder mms "link for the image"
Options:
    -h --help Show this Screen
    -m        Type the remainder you want on your phone

"""

from docopt import docopt
from twilio.rest import Client
import os

def send_message(text):
    auth_token  = os.environ["TWILIO_API"] 
    account_sid = os.environ["TWILIO_SID"]
    phone = Client(account_sid,account_sid)
    remainder = phone.messages.create(
        to=os.environ["YOUR_NUMBER"],         
        from_=os.environ["TWILIO_NUMBER"],
        body =text
        )


x = input("Enter text")
send_message(x)
