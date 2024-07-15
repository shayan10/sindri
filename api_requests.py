import os
import requests
import dotenv

dotenv.load_dotenv()

API_TOKEN = os.getenv("HF_TOKEN")

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/shayan283/multilabel_classification"
def query(payload):
    payload["parameters"] = {"candidate_labels": ["FIRST_PARTY_COLLECTION",
        "THIRD_PARTY_COLLECTION", "DATA_SECURITY", "DATA_RETENTION", "USER_CHOICE_CONTROL",
        "OTHER"]}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query({"inputs": "We are not responsible for the privacy practices of our service providers and business partners, and the information practices of these service providers and business partners are not covered by this Privacy Policy.We may aggregate or de-identify the information described above."})
print(data)