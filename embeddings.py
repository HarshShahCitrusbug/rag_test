# Imports
import openai
from pinecone import Pinecone
import os

# Third party imports
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

PINECONE_INDEX = os.getenv("PINECONE_INDEX")

pinecone_obj = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pinecone_obj.Index(PINECONE_INDEX)


def open_ai_embeddings(text: str) -> list:
    """
    Generates an embedding for the given text using OpenAI's embedding model.

    This function uses the OpenAI API to create an embedding for the provided text
    with the model "text-embedding-ada-002". It returns the embedding vector.

    :param text: The input text for which the embedding is to be generated.
    :return: A list representing the embedding vector for the input text.
    """
    response = openai.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding


def add_embeddings_to_pinecone(id: str, embedding: list, data: dict) -> None:
    """
    Adds the embeddings vector to the Pinecone index with the given ID.

    This function takes in the ID of the document, the embeddings vector, and the
    data associated with the document. It then adds the embeddings vector to the
    Pinecone index with the given ID.

    :param id: The ID of the document to add the embeddings to.
    :param embedding: The embeddings vector for the document.
    :param data: The data associated with the document.
    :return: None
    """
    index.upsert(vectors=[(id, embedding, data)])
