<<<<<<< HEAD
# 🤖 AI Email Agent (FastAPI + Ollama + Gmail Automation)

An intelligent email automation system that reads Gmail messages, generates professional replies using a local AI model (DeepSeek via Ollama), and sends responses automatically. The system also exposes a FastAPI backend for API control and integration with other applications.

---

## ✨ Features

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Ollama](https://img.shields.io/badge/Ollama-LLM-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

📥 **Automatic Email Reading**
Reads incoming Gmail messages using Gmail API.

🧠 **AI-Powered Reply Generation**
Uses DeepSeek-R1 running locally via Ollama to generate professional replies.

📤 **Automatic Reply Sending**
Sends replies automatically to human senders.

🛡️ **Smart Filtering**
Ignores system emails, spam, and self-generated messages to prevent loops.

🧠 **Persistent Memory (ChromaDB)**
Stores emails and embeddings for future retrieval and context awareness.

⚡ **FastAPI Backend Integration**
Exposes endpoints to read and reply to emails programmatically.

🌐 **Public Deployment Ready**
Can be exposed publicly using Cloudflare Tunnel or deployed to cloud platforms.

🔄 **Fully Automated Mode**
Runs continuously and replies automatically without manual intervention.

---

## 🏗️ Architecture

```text
User → Gmail → Gmail API → FastAPI → AI Agent → Ollama (DeepSeek)
                                      ↓
                                   ChromaDB
                                      ↓
                                   Gmail Send API
```

---

## 📁 Project Structure

```text
ai-email-agent/
│
├── api.py                # FastAPI backend
├── main.py               # Fully automated agent loop
├── gmail_reader.py      # Reads Gmail messages
├── gmail_sender.py      # Sends replies
├── email_agent.py      # AI reply generation
├── email_filter.py     # Filters unwanted emails
├── email_utils.py      # Email processing utilities
├── vector_store.py     # ChromaDB memory system
├── requirements.txt    # Dependencies
├── .gitignore          # Security exclusions
=======
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
>>>>>>> 40515af1796b399b0241607ccce2c6add0d1a938
└── README.md
```

---

<<<<<<< HEAD
## 🚀 Installation

Clone the repository:

```bash
=======
## Installation

Clone repository:

```
>>>>>>> 40515af1796b399b0241607ccce2c6add0d1a938
git clone https://github.com/YOUR_USERNAME/ai-email-agent.git
cd ai-email-agent
```

Create virtual environment:

<<<<<<< HEAD
```bash
=======
```
>>>>>>> 40515af1796b399b0241607ccce2c6add0d1a938
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

<<<<<<< HEAD
```bash
=======
```
>>>>>>> 40515af1796b399b0241607ccce2c6add0d1a938
pip install -r requirements.txt
```

---

<<<<<<< HEAD
## 🧠 Install Ollama and DeepSeek

Install Ollama:

https://ollama.com

Run DeepSeek model:

```bash
=======
## Setup Ollama

Install Ollama from:

https://ollama.com

Run model:

```
>>>>>>> 40515af1796b399b0241607ccce2c6add0d1a938
ollama run deepseek-r1:8b
```

---

<<<<<<< HEAD
## 📧 Gmail API Setup
=======
## Setup Gmail API
>>>>>>> 40515af1796b399b0241607ccce2c6add0d1a938

1. Go to Google Cloud Console
2. Enable Gmail API
3. Create OAuth credentials
<<<<<<< HEAD
4. Download `credentials.json`
5. Place it in project root
6. Run project once to generate `token.json`

---

## ⚡ Run FastAPI Backend

```bash
uvicorn api:app --reload
```

Open API dashboard:

```text
=======
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
>>>>>>> 40515af1796b399b0241607ccce2c6add0d1a938
http://127.0.0.1:8000/docs
```

---

<<<<<<< HEAD
## 📡 API Endpoints

### Check latest email

```http
GET /check-email
```

Returns sender and message content.

---

### Send automatic reply

```http
POST /auto-reply
```

Reads email and sends AI-generated reply.

---

## 🔄 Run Fully Automated Agent

```bash
python main.py
```

The agent will:

* Check emails every 30 seconds
* Generate reply
* Send reply automatically

---

## 🌐 Free Public Deployment

Use Cloudflare Tunnel:

```bash
cloudflared tunnel --url http://localhost:8000
```

Public API example:

```text
https://your-agent.trycloudflare.com/docs
=======
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
>>>>>>> 40515af1796b399b0241607ccce2c6add0d1a938
```

---

<<<<<<< HEAD
## 🛡️ Security

Never upload:

```text
=======
## Security Note

Never upload:

```
>>>>>>> 40515af1796b399b0241607ccce2c6add0d1a938
credentials.json
token.json
```

These files are excluded using `.gitignore`.

---

<<<<<<< HEAD
## 💡 Example Workflow

1. User sends email
2. Agent reads email
3. AI generates reply
4. Reply sent automatically
5. Email stored in memory

---

## 🧠 Technologies Used

* FastAPI
* LangChain
* Ollama
* DeepSeek-R1
* Gmail API
* ChromaDB
* Python

---

## 👤 Author

**Vikas Pandit**

---

## 📜 License

MIT License

---

## 🚀 Future Improvements

* Web dashboard
* Multi-account support
* Cloud deployment
* Email analytics
* Slack / WhatsApp integration
=======
## Author

Vikas Pandit

---

## Future Improvements

* Web dashboard
* Multi-email support
* Scheduling and analytics
* Cloud deployment
>>>>>>> 40515af1796b399b0241607ccce2c6add0d1a938
