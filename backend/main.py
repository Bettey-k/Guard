from fastapi import FastAPI
from db import models, database
from api.routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Guard AI Backend")


#  Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Guard Backend Running Successfully"}

app.include_router(api_router)
