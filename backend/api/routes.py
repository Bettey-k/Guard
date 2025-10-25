from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import models, database
from ai.model import analyze_text
from fastapi.encoders import jsonable_encoder

router = APIRouter()
@router.post("/analyze")
def analyze(text: str, db: Session = Depends(database.get_db)):
    result = analyze_text(text)[0]
    entry = models.Analysis(text=text, label=result['label'], score=result['score'])
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return {"input": text, "label": result['label'], "score": result['score']}

from fastapi.encoders import jsonable_encoder

@router.get("/history")
def get_history(db: Session = Depends(database.get_db)):
    records = db.query(models.Analysis).all()
    return jsonable_encoder(records)
