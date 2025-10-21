# 🛡️ Guard – AI Racism Prevention System

## 📖 Overview
**Guard** is an AI-powered system that detects racist and hate speech content across social media platforms — with a special focus on **Amharic language**.  
It helps moderators and officials prevent the spread of offensive content automatically.

---

##  Purpose
- Detect offensive content in **Amharic** and **English**.
- Assist moderation teams with **real-time alerts**.
- Provide **analytics dashboards** to visualize trends in racist or hateful content.

---

## Key Features
- 🧠 AI-based text classification (Hugging Face model)
- ⚙️ FastAPI backend for data processing
- 💾 PostgreSQL database for storing messages and logs
- 🌐 Next.js dashboard for analytics and moderation
- 🔔 Telegram or email alerts for flagged content
- 📑 Step-by-step setup guide for beginners

---

## 🧰 Tech Stack

| Layer | Technology |
|--------|-------------|
| **AI Model** | hugging face |
| **Backend** | Python + FastAPI |
| **Database** | PostgreSQL |
| **Frontend** | Next.js + TailwindCSS |
| **Social Media Integration** | Telegram API via Telethon |
| **Deployment** | Docker Compose |
| **Version Control** | Git + GitHub |
| **Alerts** | Telegram Bot / Email Notifications |

---

##  Architecture Overview

flowchart LR
    A[Social Media (Telegram/Facebook)] --> B[Listener (Telethon)]
    B --> C[FastAPI Backend]
    C --> D[PostgreSQL Database]
    C --> E[Next.js Dashboard]
    C --> F[Alerts System (Telegram/Email)]


---

## 📂 Folder Structure

guard/
├── backend/
│   ├── ai/
│   ├── api/
│   ├── db/
│   └── utils/
├── frontend/
│   ├── dashboard
├── telegram_listener/
├── docs/
└── docker-compose.yml

---

## 👩‍💻 Project Status
- Currently in **development phase**
- Beginner-friendly documentation prepared
- Core backend setup in progress

---
