#! /usr/bin/env python3
"""terminaltext

Usage:
    terminaltext -m <text>
    terminaltext -mms <link>

Options:
  -h --help     Show this screen.
  --version     Show version.
  -m            Send Message a remainder to the phone.
  -mms          Sending a picture
"""

from docopt import docopt
from twilio.rest import Client
import os


def send_remainder(text):
    auth_token  = os.environ["TWILIO_API"] 
    account_sid = os.environ["TWILIO_SID"]
    phone = Client(account_sid,account_sid)
    remainder = phone.messages.create(
        to=os.environ["YOUR_NUMBER"],         
        from_=os.environ["TWILIO_NUMBER"],
        body =text
        )


def mms(link):
    auth_token  = os.environ["TWILIO_API"] 
    account_sid = os.environ["TWILIO_SID"]
    phone = Client(account_sid,account_sid)
    remainder = phone.messages.create(
        to=os.environ["YOUR_NUMBER"],         
        from_=os.environ["TWILIO_NUMBER"],
        media_url =link
        )


if __name__ == '__main__':

    arguments = docopt(__doc__,version='Terminal Text-1.0')
    
    if arguments['-m']:
        send_remainder(arguments['<text>'])
    elif arguments['-mms']:
        mms(arguments['<link>'])