import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient
from config import *

def extract_text_from_blob(blob_name):
    # Connect to Azure Document Intelligence
    document_client = DocumentAnalysisClient(AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT, AzureKeyCredential(AZURE_DOCUMENT_INTELLIGENCE_KEY))

    # Connect to Azure Blob Storage
    blob_service_client = BlobServiceClient(account_url=f"https://{AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net", credential=AZURE_STORAGE_ACCOUNT_KEY)
    blob_client = blob_service_client.get_blob_client(container=AZURE_STORAGE_CONTAINER_NAME, blob=blob_name)

    # Download file from blob storage
    pdf_data = blob_client.download_blob().readall()

    # Analyze PDF document
    poller = document_client.begin_analyze_document("prebuilt-layout", pdf_data)
    result = poller.result()

    extracted_text = " ".join([line.content for page in result.pages for line in page.lines])
    return extracted_text

# Example usage
if __name__ == "__main__":
    text = extract_text_from_blob("sample_document.pdf")
    print(text)
