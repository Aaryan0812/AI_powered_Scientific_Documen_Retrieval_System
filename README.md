

# **Intelligent Scientific Document Retrieval System 🚀**  

## **Project Overview**  
This project is an **AI-powered document retrieval system** designed for **scientific and pharmaceutical research**. It allows researchers to query **chemical and pharmaceutical documents** using **natural language** and retrieves precise information with citations.  

## **Key Features**  
✅ **Extracts key information** (chemical formulas, molecular structures, metadata) from PDFs.  
✅ **Embeds document content** using **GPT-4o** for **semantic search**.  
✅ **Indexes embeddings** in **Azure AI Search** for **efficient vector retrieval**.  
✅ **Serves search queries** via a **FastAPI REST API**.  
✅ **Uses Azure ADLS** as the storage backend for documents.  

---

## **Tech Stack**  
| Component                 | Technology Used |
|---------------------------|----------------|
| **Document Storage**      | Azure ADLS (Blob Storage) |
| **Data Extraction**       | Azure Document Intelligence |
| **Embeddings & AI Model** | GPT-4o (Azure OpenAI) |
| **Vector Database**       | Azure AI Search |
| **API Framework**         | FastAPI |
| **Storage Access**        | Azure SDK for Python |
| **Deployment**           | Uvicorn |

---

## **Architecture** 🏗  
1. **Documents** are stored in **Azure Blob Storage** (`Scientific_doc` container).  
2. **Azure Document Intelligence** extracts text, molecular formulas, and metadata.  
3. **GPT-4o** generates **semantic embeddings** for the text.  
4. **Azure AI Search** indexes these embeddings for fast retrieval.  
5. **FastAPI** serves a **REST API** for querying documents.  

---


## **Future Enhancements**  
🚀 **Add support for multi-modal retrieval (images + text)**  
🔎 **Improve ranking of retrieved documents**  
📄 **Enhance PDF processing with advanced OCR**  

