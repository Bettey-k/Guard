# ⚙️ Guard Project Setup Guide (Beginner Friendly)

This guide helps you set up and run the **Guard AI Racism Prevention System** on your local computer using VS Code.

---

## 🧰 Prerequisites

Before starting, make sure these tools are installed and verified:

| Tool | Check Command |
|------|----------------|
| Python 3.10+ | `python --version` |
| Pip | `pip --version` |
| Git | `git --version` |
| Node.js & npm | `node -v` and `npm -v` |
| Docker Desktop | `docker --version` |
| PostgreSQL | `psql --version` 
| VS Code | Installed and working |

---

## 🏗️ 1. Clone or Create Project Folder

If you have a GitHub repo:
```bash
git clone https://github.com/yourusername/guard.git
cd guard
```

Or create it manually:
- Open VS Code → “File” → “Open Folder” → name it **guard**

---

## ⚙️ 2. Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
venv\Scripts\activate    # (Windows)
source venv/bin/activate # (Mac/Linux)

pip install -r requirements.txt
```
continue.......