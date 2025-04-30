from fastapi import FastAPI
from pydantic import BaseModel
from tools.diagnosis_tool import get_diagnosis
from tools.symptom_extractor import extract_symptoms
from tools.pubmed_fetcher import fetch_pubmed_articles_with_metadata
from tools.summarizer import summarize_text

app = FastAPI()

class SymptomInput(BaseModel):
    description:str

@app.post("/diagnosis")
def diagnose_patient(data:SymptomInput):
    symptoms = extract_symptoms(data.description)
    diagnosis = get_diagnosis(symptoms)
    pubmed_articles = fetch_pubmed_articles_with_metadata(" ".join(symptoms))
    pubmed_text = " ".join([article["abstract"] for article in pubmed_articles])
    summary = summarize_text(pubmed_text[:3000])
    
    return {
        "symptom":symptoms,
        "diagnosis":diagnosis,
        "pubmed_summary" :summary
    }
    