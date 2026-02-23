from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import base64
from email.mime.text import MIMEText


SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send'
]


def send_reply(reply_text, to_email):

    creds = Credentials.from_authorized_user_file(
        'token.json', SCOPES)

    service = build('gmail', 'v1', credentials=creds)

    message = MIMEText(reply_text)

    message['to'] = to_email

    message['subject'] = "Re: Your Email"

    raw = base64.urlsafe_b64encode(
        message.as_bytes()).decode()

    body = {
        'raw': raw
    }

    service.users().messages().send(
        userId='me',
        body=body
    ).execute()

    print("\nReply sent successfully.")