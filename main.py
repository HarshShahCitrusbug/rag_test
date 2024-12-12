# Third party imports here
import streamlit as st
import os

# Local imports here
from dotenv import load_dotenv
from pinecone import Pinecone

# Local imports here
from pinecone_service import query_from_pinecone, upsert_text_to_pinecone
from utils import get_text_from_docx

load_dotenv()

# Pinecone index
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

FILE_PATH_1 = "Client 001_CoachingSession_03.12.24.docx"
FILE_PATH_2 = "Client 001_CoachingSession_10.12.24.docx"
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

text_1_embeddings = get_text_from_docx(FILE_PATH_1)
text_2_embeddings = get_text_from_docx(FILE_PATH_2)

pinecone = Pinecone(api_key=PINECONE_API_KEY)
index_name = PINECONE_INDEX


index = pinecone.Index(index_name)


# upsert_text_to_pinecone(text_1_embeddings, index)
# upsert_text_to_pinecone(text_2_embeddings, index)

# Streamlit App
def main():
    st.title("Vector Search")

    query = st.text_input("Enter your query:")

    # Add a 'Search' button
    search_button = st.button("Search")

    # Display search results when the button is clicked
    if search_button and query:
        search_results = query_from_pinecone(query)
        if search_results:
            # Display the matched document text
            st.write(search_results['matches'][0]['metadata']['text'])
        else:
            st.write("No results found")


if __name__ == "__main__":
    main()
