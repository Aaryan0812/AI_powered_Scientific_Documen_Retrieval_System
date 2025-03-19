import requests
import json
from config import *

def index_document(document_id, text, embedding):
    url = f"https://{AZURE_AI_SEARCH_SERVICE_NAME}.search.windows.net/indexes/{AZURE_AI_SEARCH_INDEX_NAME}/docs/index?api-version=2023-07-01-preview"
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_AI_SEARCH_API_KEY
    }
    
    document = {
        "value": [
            {
                "@search.action": "upload",
                "id": document_id,
                "content": text,
                "embedding": embedding
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=document)
    return response.json()

# Example usage
if __name__ == "__main__":
    sample_text = "This is a sample scientific document about molecules."
    embedding = generate_embedding(sample_text)
    response = index_document("doc_001", sample_text, embedding)
    print(response)
