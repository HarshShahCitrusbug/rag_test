# Imports here
import os

# Third party imports here
from pinecone import Pinecone
from dotenv import load_dotenv

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
    result = index.query(namespace="bhagvat1", top_k=5,
                         include_values=True, query=query, include_metadata=True)
    return result
