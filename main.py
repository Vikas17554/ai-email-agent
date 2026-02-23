import time

from gmail_reader import read_latest_email
from email_agent import process_email
from vector_store import save_email
from email_filter import is_human_email
from gmail_sender import send_reply
from email_utils import extract_email


print("AI Email Agent started...")
print("Press CTRL + C to stop.\n")


last_email = None


try:

    while True:

        sender, email = read_latest_email()
        if sender.lower().find("rajupandit841995@gmail.com") != -1:
            print("Ignoring own email.")
            time.sleep(60)
            continue

        # Check if new email
        if email != last_email:

            print("\n==============================")
            print("New email detected!")
            print("==============================")

            print("\nSender:", sender)

            print("\nSender's message:")
            print(email)

            print("\n--------------------------")

            if is_human_email(sender):

                print("Human email detected. Generating reply...")

                save_email(email)

                result = process_email(email)

                print("Reply:\n", result)

                to_email = extract_email(sender)

                send_reply(result, to_email)

            else:

                print("Company/System email. No reply sent.")

            last_email = email

        else:

            print("No new email.")

        # wait 30 seconds
        time.sleep(30)


except KeyboardInterrupt:

    print("\n\nAI Email Agent stopped.")