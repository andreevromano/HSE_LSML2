from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
from transformers import BertForSequenceClassification, BertTokenizerFast
from typing import List

class ReviewText(BaseModel):
    text: str

class ReviewTexts(BaseModel):
    texts: List[str]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Указать конкретные домены в продакшене
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = "./saved_model"
tokenizer = BertTokenizerFast.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)
model.eval()

def predict_single(text):
    inputs = tokenizer(text, truncation=True, padding=True, max_length=128, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    preds = torch.argmax(logits, dim=-1).item()
    sentiment = "positive" if preds == 1 else "negative"
    return sentiment

@app.post("/predict")
def predict_sentiment(data: ReviewText):
    sentiment = predict_single(data.text)
    return {"text": data.text, "sentiment": sentiment}

@app.post("/predict_batch")
def predict_sentiment_batch(data: ReviewTexts):
    results = []
    for t in data.texts:
        sentiment = predict_single(t)
        results.append({"text": t, "sentiment": sentiment})
    return {"results": results}
