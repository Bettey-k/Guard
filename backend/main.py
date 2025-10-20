#FAST API ENTRY POINT
from fastapi import FastAPI
from ai.model import analyze_text
#initialize FastAPI app
app  = FastAPI(title="Guard AI Backend")
#home endpoint
@app.get("/")
def home():
    return{"message":"Guard Backend Running Successfully"}

@app.post("/analyze")
def analyze(text: str):
    """
    Analyze Amharic or English text using AI model.
    """
    result=analyze_text(text)
    return {"input": text,"analyze":result}
