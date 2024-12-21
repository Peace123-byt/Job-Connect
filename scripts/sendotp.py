from twilio.rest import Client

# Replace these with your Twilio Account SID and Auth Token
account_sid = 'ACca8e92f22a9545888981187f2ac15213'
auth_token = '2be85a707169a4f453e9dba5591db82d'

# Create a Twilio client
client = Client(account_sid, auth_token)
# Replace these with your Twilio phone number and the recipient's mobile number
from_number = '+12294849446'
to_number = '+19419496785'

# The message you want to send
message_body = 'Testing sms by the backend Team lead!'

# Send the SMS
message = client.messages.create(
    from_=from_number,
    body=message_body,
    to=to_number
)

# Print the SID (a unique identifier) of the sent message
print(f"Message SID: {message.sid}")