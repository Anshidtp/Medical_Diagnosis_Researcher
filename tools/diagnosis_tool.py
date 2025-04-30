import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

client = Groq(api_key=os.getenv("LLM_API_KEY"))



def get_diagnosis(symptoms: list[str]) -> str:
    prompt = f"Patient has symptoms: {', '.join(symptoms)}. Suggest possible medical diagnoses.suggest me a possible cure fro the same"

    response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": prompt}
        ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
    )

    return response.choices[0].delta.content.strip()
