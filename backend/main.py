from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from ai.model import analyze_text
from db.database import Base, engine, get_db
from db.models import Analysis

# Initialize FastAPI
app = FastAPI(title="Guard AI Backend")

# Create tables automatically
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Guard Backend Running Successfully"}

@app.post("/analyze")
def analyze(text: str, db: Session = Depends(get_db)):
    result = analyze_text(text)
    label = result[0]["label"]
    score = result[0]["score"]

    # Save to database
    new_entry = Analysis(text=text, label=label, score=score)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return {"input": text, "analyze": result}
