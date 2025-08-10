import chromadb
from chromadb.utils import embedding_functions

chroma_client = chromadb.Client()
chroma_collection = chroma_client.get_or_create_collection("chapters")

def store_version(version_text, meta={}):
    chroma_collection.add(
        documents=[version_text],
        metadatas=[meta],
        ids=[f"id_{meta['version']}"]
    )
