from google.oauth2 import service_account, credentials
import oauth2client
from google.oauth2.credentials import Credentials
import base64
from email.message import EmailMessage

from google.auth.credentials import CredentialsWithQuotaProject
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import json
import os

EMAIL_FROM = "vivualtvick@gmail.com"

CLIENT_ID = "891838441976-3jlrcc18kr5nongnq90thrlr7l69mcvl.apps.googleusercontent.com"

CLIENT_SECRETE = "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"

AUTHORIZATION_CODE = "4/0AWtgzh5t-C29JzybMGrPkNz9A16kIqvLsYub9Q3hTynrxla1m4hx2WBYfDXew9dnZjx-hg"

REFRESH_TOKEN = "1//048r92qcXjUocCgYIARAAGAQSNwF-L9IrJSWufrNU7jqlONZz0R6_cGPRTME8DBSmRgIL8yFCtu7YK2krq8GJZ0wCXskSYG5IIyI"

ACCESS_TOKEN = "ya29.a0AVvZVsqLExdNGeYIdUFgvxMjhytv5HNyQ8X0aIMIU-OE6MfyOQjzeqTAFza5Bm0vCn3eFHASEYcHeCChVmU_uHZK-DguUU9GvBM07dmvnQV1R-K7khy0jX3NkmNYrY681ifg7bBQkGpYZBaf5p4nNdDMoizxaCgYKAbcSARISFQGbdwaIz2JXJY2V7PMApWKl3EYQ3w0163"


SCOPES = ['https://www.googleapis.com/auth/gmail.send']
SERVICE_ACCOUNT_FILE = 'C:\\Users\\vicky\\Desktop\\projects\\taskApp\\root\\mainapp\\cred.json'
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = credentials.with_subject(EMAIL_FROM)

def get_credentials():
    # If needed create folder for credential
    home_dir = os.path.expanduser('~') #>> C:\Users\Me
    credential_dir = os.path.join(home_dir, '.credentials') # >>C:\Users\Me\.credentials   (it's a folder)
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)  #create folder if doesnt exist
    credential_path = os.path.join(credential_dir, 'cred send mail.json')

    #Store the credential
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()

    if not credentials or credentials.invalid:
        CLIENT_SECRET_FILE = 'client_id to send Gmail.json'
        APPLICATION_NAME = 'Gmail API Python Send Email'
        #The scope URL for read/write access to a user's calendar data  

        SCOPES = 'https://www.googleapis.com/auth/gmail.send'

        # Create a flow object. (it assists with OAuth 2.0 steps to get user authorization + credentials)
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME

        credentials = tools.run_flow(flow, store)

    return credentials




def gmail_create_draft():
    """Create and insert a draft email.
       Print the returned draft's message and id.
       Returns: Draft object, including draft id and message meta data.

      Load pre-authorized user credentials from the environment.
      TODO(developer) - See https://developers.google.com/identity
      for guides on implementing OAuth2 for the application.
    """
    creds = credentials

    try:
        # create gmail api client
        service = build('gmail', 'v1', credentials=delegated_credentials)

        message = EmailMessage()

        message.set_content('This is automated draft mail')

        message['To'] = 'developervick@gmail.com'
        message['From'] = 'vivualtvick@gmail.com'
        message['Subject'] = 'automated api mail'

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {
            'message': {
                'raw': encoded_message
            }
        }
        # pylint: disable=E1101
        draft = service.users().drafts().create(userId="me",
                                                body=create_message).execute()

        print(F'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        draft = None

    return draft


if __name__ == '__main__':
    gmail_create_draft()