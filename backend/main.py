from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"message":"Hello World"}
# from pypdf import PdfReader
# from sentence_transformers import SentenceTransformer
# import os
# import re
# from qdrant_client import QdrantClient
# from qdrant_client.models import Distance, VectorParams, PointStruct, Document
# from dotenv import load_dotenv
# from openai import OpenAI
# from pydantic import BaseModel


# import uuid
# import os
# import re

# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# QDRANT_URL = os.getenv("QDRANT_URL")
# QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
# app = FastAPI()
# model = SentenceTransformer("all-MiniLM-L6-v2")
# openai_client = OpenAI(api_key=OPENAI_API_KEY)
# qdrant = QdrantClient(
#     url=os.getenv("QDRANT_URL"),
#     api_key=os.getenv("QDRANT_API_KEY"),
# )


# # create collection
# COLLECTION_NAME = "pdf_chunks"
# collections = qdrant.get_collections()
# existing = [
#     c.name
#     for c in collections.collections
# ]
# if COLLECTION_NAME not in existing:
#     qdrant.create_collection(
#         collection_name=COLLECTION_NAME,
#         vectors_config=VectorParams(
#             size=384,
#             distance=Distance.COSINE
#         )
#     )

# # cleaning the text
# def clean_text(text):
#     text = re.sub(r'\s+',' ',text)
#     return text.strip()

# # chunking the text
# def chunk(text,chunk_size=1000,chunk_overlap=200):
#     chunks = []
#     for i in range(0, len(text), chunk_size):
#         chunks.append(text[i:i+chunk_size])
#     return chunks


# @app.get("/health")
# def health_check():
#     return {"message":"Server is running"}
# class ChatRequest(BaseModel):
#     filename:str
#     question:str

# @app.post("/upload-pdf")
# async def upload_pdf(file: UploadFile = File(...)):

#     # save pdf in the upload folder
#     path = os.path.join("upload", file.filename)
#     with open(path, "wb") as f:
#         f.write(await file.read())

#     pdf_reader = PdfReader(path)

#     text = ""
#     for page in pdf_reader.pages:
#         text += page.extract_text()

#     cleaned_text = clean_text(text)
#     page_chunk = chunk(cleaned_text)
#     embeddings = model.encode(page_chunk)
#     cleaned_text = clean_text(text)   #cleaning the text
#     page_chunk = chunk(cleaned_text)   #chunking the text
#     embeddings = model.encode(page_chunk)   #encoding the text

#     points = []
#     for idx, (chunk, embedding) in enumerate(
#         zip(page_chunk, embeddings)
#     ):

#         points.append(
#             PointStruct(
#                 id=str(uuid.uuid4()),
#                 vector=embedding.tolist(),
#                 payload={
#                     "filename":
#                         file.filename,

#                     "chunk_id":
#                         idx,

#                     "text":
#                         chunk
#                 }
#             )
#         )

#     qdrant.upsert(
#         collection_name=COLLECTION_NAME,
#         points=points
#     )

#     return {
#         "filename": file.filename,
#         "saved":path,
#         "charecter_count": len(text),
#         "preview": text[:100],
#         "first_chunk": page_chunk[0]
#     }
#         "saved":path,   #saving the pdf
#         "charecter_count": len(text),   #counting the characters
#         "preview": text[:100],   #previewing the text
#         "first_chunk": page_chunk[0]   #first chunk of the text
#     }  #returning the data

# @app.get("/doccuments")
# def get_document():
#     return {
#         "uploaded doccuments": list(documents.keys())
#     }

# @app.get("/document/{filename}")
# def get_document_by_filename(filename: str):
#     if filename not in documents:
#         return{
#             "error": "File not found"
#         }
#     return {
#         "filename":filename,
#         "embeddings": list(documents[filename]["embeddings"].shape),
#     }


# @app.post("/search")
# def search_pdf(request:ChatRequest):
#     query_embedding = (
#         model.encode(
#             request.question
#         ).tolist()
#     )
#     results = qdrant.search(
#         collection_name=COLLECTION_NAME,
#         query_vector=query_embedding,
#         limit=3
#     )
#     chunks = []
#     for result in results:
#         chunks.append(
#             result.payload["text"]
#         )
#     return {
#         "results": chunks
#     }


# # upload Pdf
# # save Pdf 
# # extract text from pdf 
# # clean text 
# # chunking of text 
# # creating embeding 
# # store it in memory / db
# # chating
# # embedding search
