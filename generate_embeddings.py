import openai
from config import *

openai.api_key = AZURE_OPENAI_API_KEY
openai.api_base = AZURE_OPENAI_ENDPOINT

def generate_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response["data"][0]["embedding"]

# Example usage
if __name__ == "__main__":
    sample_text = "This is a sample scientific research document."
    embedding = generate_embedding(sample_text)
    print(embedding)
