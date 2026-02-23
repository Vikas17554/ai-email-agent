from langchain_ollama import ChatOllama
import re

llm = ChatOllama(model="deepseek-r1:8b")

def process_email(email):

    prompt = f"""
You are Vikas Pandit replying to an email.

Your job is to generate a professional reply immediately.

STRICT RULES:
- NEVER use placeholders like [Name], [Your Name], [Date], [Time], etc.
- NEVER use square brackets [] in the reply.
- If the email contains a specific time or date, use that exact time/date.
- If the email does NOT contain time/date, say "I will be available" instead of guessing.
- Use the name "Vikas" as the sender.
- DO NOT include Subject.
- DO NOT include explanation.
- ONLY output the reply message body.
- Keep reply short and professional (3–5 lines).
- End the reply with your name: Vikas

Email received:
{email}

Reply:
"""

    response = llm.invoke(prompt)

    reply = response.content.strip()

    # Remove any bracket placeholders if model still generates them
    reply = re.sub(r"\[.*?\]", "", reply)

    # Ensure reply ends with Vikas
    if not reply.endswith("Vikas"):
        reply = reply + "\n\nVikas"

    return reply