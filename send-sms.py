import os
import sys
from twilio.rest import TwilioRestClient



account = "ACXXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account, token)

ADMIN="+1XXXXXX"


message = client.messages.create(to=ADMIN, from_="+1XXXXX",
                                         body="Intruder alert @ Lowell Makes")

