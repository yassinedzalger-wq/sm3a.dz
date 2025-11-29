from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI(title="سمعة DZ")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def home():
    return {"message": "سمعة DZ شغالة في الجزائر الآن 🇩🇿"}

@app.get("/search/{company}")
def search(company: str):
    # نموذج عربي مجاني 100%
    hf_response = requests.post(
        "https://api-inference.huggingface.co/models/marefa-ai/Arabic-Sentiment",
        json={"inputs": f"الخبر عن {company} في الجزائر"},
        timeout=10
    )
    sentiment = "محايد"
    if hf_response.status_code == 200:
        result = hf_response.json()
        if result and len(result[0]) > 0:
            sentiment = "إيجابي" if result[0][0]["label"] == "POS" else "سلبي"

    return {
        "company": company,
        "alerts": [
            {"text": f"خبر جديد عن {company} في وكالة الأنباء الجزائرية", "sentiment": sentiment, "source": "APS.dz"},
            {"text": f"منشور فيسبوك عن {company}", "sentiment": "إيجابي", "source": "فيسبوك"},
            {"text": f"تغريدة على X عن {company}", "sentiment": sentiment, "source": "X.com"}
        ]
    }
