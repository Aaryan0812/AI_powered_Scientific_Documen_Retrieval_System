from fastapi import FastAPI
from search import search_documents

app = FastAPI()

@app.get("/search/")
def search(query: str):
    results = search_documents(query)
    return results

# Run FastAPI: uvicorn main:app --reload
