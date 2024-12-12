# Imports here
import os

# Third party imports here
from pinecone import Pinecone
from dotenv import load_dotenv

# Local imports here
from embeddings import open_ai_embeddings
from utils import convert_text_into_chunks

# Load environment variables
load_dotenv()

# Pinecone index
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


pinecone = Pinecone(api_key=PINECONE_API_KEY)

index = pinecone.Index(PINECONE_INDEX)


def query_from_pinecone(query: str):
    """
    Function to query the Pinecone index with the given query string.
    Returns the results from Pinecone.
    """
    # Perform the query using Pinecone's query method
    # Get top 5 results, adjust as needed
    query_embedding = open_ai_embeddings(query)
    result = index.query(top_k=5, vector=query_embedding,
                         include_metadata=True)
    return result


def upsert_text_to_pinecone(text, index):
    chunks = convert_text_into_chunks(text)
    vectors = []
    for i, chunk in enumerate(chunks):
        embedding = open_ai_embeddings(chunk)
        # Store each chunk with a unique ID
        vectors.append((f"chunk-{i}", embedding, {"text": chunk}))
    index.upsert(vectors=vectors)
