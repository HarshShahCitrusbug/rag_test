# Imports here
import os

# Third party imports here
from pinecone import ServerlessSpec, Pinecone
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Pinecone index
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


pinecone = Pinecone(api_key=PINECONE_API_KEY)


def create_pinecone_index():
    """
    Function to create the Pinecone index.
    """
    index_name = PINECONE_INDEX
    # Create the Pinecone index
    if index_name not in pinecone.list_indexes().names():
        pinecone.create_index(
            name=index_name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )


# Call the create_pinecone_index function
create_pinecone_index()
