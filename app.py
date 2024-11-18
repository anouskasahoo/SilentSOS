from dotenv import load_dotenv
import os
#from twilio.rest import Client
import requests

url = 'https://textbelt.com/text'

#load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
recipient_number = os.getenv('RECIPIENT_PHONE_NUMBER')


print("Account SID:", account_sid)
print("Auth Token:", auth_token)
print("Twilio Number:", twilio_number)
print("Recipient Number:", recipient_number)


client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello, this is a test message from Twilio!",
    from_=twilio_number,
    to=recipient_number
)

print(f"Message SID: {message.sid}")


data = {
    'phone': '+919871437916',
    'message': 'SOS! Send Help!',
    'key': 'textbelt'
}

response = requests.post(url, data)

print(response.json())