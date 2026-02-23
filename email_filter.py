def is_human_email(sender):

    your_email = "rajupandit841995@gmail.com"

    sender_lower = sender.lower()

    # Block self emails
    if your_email in sender_lower:
        return False

    # Block system emails
    blocked = [
        "noreply",
        "no-reply",
        "google",
        "notification",
        "alert",
        "support"
    ]

    for word in blocked:
        if word in sender_lower:
            return False

    return True