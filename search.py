import requests
import json
from config import *

def search_documents(query):
    url = f"https://{AZURE_AI_SEARCH_SERVICE_NAME}.search.windows.net/indexes/{AZURE_AI_SEARCH_INDEX_NAME}/docs/search?api-version=2023-07-01-preview"
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_AI_SEARCH_API_KEY
    }
    
    request_payload = {
        "search": query,
        "vectorQueries": [
            {
                "kind": "vector",
                "fields": "embedding",
                "value": generate_embedding(query),
                "k": 5  # Retrieve top 5 documents
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=request_payload)
    return response.json()

# Example usage
if __name__ == "__main__":
    results = search_documents("molecular structure analysis")
    print(json.dumps(results, indent=2))
