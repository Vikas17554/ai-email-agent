from fastapi import FastAPI

from gmail_reader import read_latest_email
from email_agent import process_email
from email_filter import is_human_email
from gmail_sender import send_reply
from email_utils import extract_email
from vector_store import save_email


app = FastAPI()


@app.get("/")
def root():
    return {"status": "AI Email Agent API running"}


@app.get("/check-email")
def check_email():

    sender, email = read_latest_email()

    return {
        "sender": sender,
        "email": email
    }


@app.post("/auto-reply")
def auto_reply():

    sender, email = read_latest_email()

    if not is_human_email(sender):

        return {
            "status": "ignored",
            "reason": "system or own email"
        }

    save_email(email)

    reply = process_email(email)

    to_email = extract_email(sender)

    send_reply(reply, to_email)

    return {
        "status": "reply sent",
        "sender": sender,
        "reply": reply
    }