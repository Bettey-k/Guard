from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db.database import get_db
from db import models
from ai.model import analyze_text

app = FastAPI(title="Guard AI Backend")

# ✅ Allow frontend (port 3000) to talk to backend (port 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows requests from any origin (you can later limit it)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Guard Backend Running Successfully"}

@app.post("/analyze")
def analyze(text: str, db: Session = Depends(get_db)):
    result = analyze_text(text)
    label = result[0]["label"]
    score = result[0]["score"]

    new_entry = models.Analysis(text=text, label=label, score=score)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return {"id": new_entry.id, "text": text, "label": label, "score": score}

@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    records = db.query(models.Analysis).order_by(models.Analysis.id.desc()).all()
    return records
