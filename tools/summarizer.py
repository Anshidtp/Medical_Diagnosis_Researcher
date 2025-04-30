# tools/summarizer.py
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("LLM_API_KEY"))

def summarize_text(text: str) -> str:
    prompt = f"Summarize the following medical abstract:\n\n{text}"

    response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
            {"role": "system", "content": "You are a medical research summarizer."},
            {"role": "user", "content": prompt}
        ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
    )

    return response.choices[0].message.content
