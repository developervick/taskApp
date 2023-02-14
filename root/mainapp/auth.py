from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import base64
from email.message import EmailMessage
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 
          'https://www.googleapis.com/auth/gmail.compose']


def get_service():

    """
    This function returns authenticated service to use google APIs
    1. To build service with oyur credentials pass the path of credential file from google workspace console.
    2. Pass scopes of your service to to scopes parameters to as python list object
    
    *** Everry time you changes scopes you have to delete token.json file from your root directory,
    to build new creds for new scopes   
    """

    creds = None

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './mainapp/api_creds_desktop.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)


        # below commented out code is default testing purpose code which returns all
        # the lables of gmail account and modified to return authenticated service to use gmail API

        #//results = service.users().labels().list(userId='me').execute()
        #//labels = results.get('labels', [])
#//
        #//if not labels:
        #//    print('No labels found.')
        #//    return
        #//print('Labels:')
        #//for label in labels:
        #//    print(label['name'])

        return service
            

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')



def gmail_send_message(reciepent_id,subject ,message , sender_id="vivualtvick@gmail.com", service=get_service()):
    
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    msg = str(message)

    try:
        message = EmailMessage()

        message.set_content(msg)

        message['To'] = reciepent_id
        message['From'] = sender_id
        message['Subject'] = subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message


#    otp boilerplace code
#
#
# totp = pyotp.TOTP('base32secret3232')
# otp = totp.now()
# print(otp)
# 
# # OTP verified for current time
# print(totp.verify(896543))
# print(totp.verify(otp)) # => False
# 