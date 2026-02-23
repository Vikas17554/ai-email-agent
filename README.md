# AI Email Agent (FastAPI + Ollama + Gmail API)

An automated AI Email Assistant that reads emails, generates professional replies using DeepSeek (via Ollama), and sends responses automatically. The system also exposes a FastAPI backend for integration with web apps, mobile apps, or automation tools.

---

## Features

* Automatically reads emails from Gmail
* Generates professional replies using local LLM (DeepSeek via Ollama)
* Sends replies automatically via Gmail API
* Filters system emails to avoid unwanted replies
* Memory support using ChromaDB
* FastAPI backend for API access
* Fully automated agent loop support
* Free deployment support using Cloudflare Tunnel

---

## Tech Stack

* Python 3.10+
* FastAPI
* LangChain
* Ollama (DeepSeek-R1 8B)
* Gmail API
* ChromaDB
* Uvicorn

---

## Project Structure

```
ai-email-agent/
│
├── api.py
├── main.py
├── gmail_reader.py
├── gmail_sender.py
├── email_agent.py
├── email_filter.py
├── email_utils.py
├── vector_store.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone repository:

```
git clone https://github.com/YOUR_USERNAME/ai-email-agent.git
cd ai-email-agent
```

Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Setup Ollama

Install Ollama from:

https://ollama.com

Run model:

```
ollama run deepseek-r1:8b
```

---

## Setup Gmail API

1. Go to Google Cloud Console
2. Enable Gmail API
3. Create OAuth credentials
4. Download credentials.json
5. Place in project root

Run once to generate token.json

---

## Run FastAPI Server

```
uvicorn api:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Check email

GET `/check-email`

### Auto reply

POST `/auto-reply`

---

## Run Fully Automated Agent

```
python main.py
```

---

## Deployment (Free)

Use Cloudflare Tunnel:

```
cloudflared tunnel --url http://localhost:8000
```

---

## Security Note

Never upload:

```
credentials.json
token.json
```

These files are excluded using `.gitignore`.

---

## Author

Vikas Pandit

---

## Future Improvements

* Web dashboard
* Multi-email support
* Scheduling and analytics
* Cloud deployment
