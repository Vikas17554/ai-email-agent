from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import base64
import os

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send'
]
def get_gmail_service():

    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    return service

def read_latest_email():

    service = get_gmail_service()

    results = service.users().messages().list(
        userId='me', maxResults=1).execute()

    messages = results.get('messages', [])

    if not messages:
        return None, None

    msg = service.users().messages().get(
        userId='me', id=messages[0]['id'], format='full').execute()

    headers = msg['payload']['headers']

    sender = ""

    for header in headers:
        if header['name'] == 'From':
            sender = header['value']

    payload = msg['payload']

    body = ""

    if 'data' in payload.get('body', {}):
        body = payload['body']['data']

    elif 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                body = part['body']['data']
                break

    if body:
        decoded = base64.urlsafe_b64decode(body).decode('utf-8')
        return sender, decoded

    return sender, ""
# def read_latest_email():

    service = get_gmail_service()

    results = service.users().messages().list(
        userId='me', maxResults=1).execute()

    messages = results.get('messages', [])

    if not messages:
        return "No emails found"

    msg = service.users().messages().get(
        userId='me', id=messages[0]['id'], format='full').execute()

    payload = msg['payload']

    body = ""

    if 'data' in payload.get('body', {}):
        body = payload['body']['data']

    elif 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                body = part['body']['data']
                break

    if body:
        decoded = base64.urlsafe_b64decode(body).decode('utf-8')
        return decoded

    return "No readable email body found"