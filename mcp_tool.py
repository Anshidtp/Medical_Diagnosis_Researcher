from fastmcp import FastMCP
from tools.diagnosis_tool import get_diagnosis
from tools.symptom_extractor import extract_symptoms
from tools.pubmed_fetcher import fetch_pubmed_articles_with_metadata
from tools.summarizer import summarize_text
mcp = FastMCP("medical disgnosis custom mcp")

@mcp.tool()
def diagnose_patient(user_input):
    symptoms = extract_symptoms(user_input.description)
    diagnosis = get_diagnosis(symptoms)
    pubmed_articles = fetch_pubmed_articles_with_metadata(" ".join(symptoms))
    pubmed_text = " ".join([article["abstract"] for article in pubmed_articles])
    summary = summarize_text(pubmed_text[:3000])
    
    return {
        "symptom":symptoms,
        "diagnosis":diagnosis,
        "pubmed_summary" :summary
    }
        
if __name__ == "__main__":
    mcp.run()