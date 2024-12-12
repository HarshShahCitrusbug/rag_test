# RAG-based Search with Pinecone Vectors

This project demonstrates the implementation of a Retrieval-Augmented Generation (RAG) model for efficient search and information retrieval using Pinecone as the vector database. The system retrieves relevant documents based on a query and generates responses by combining the retrieval results with the generative model.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Setting up Pinecone](#setting-up-pinecone)
  - [Running the RAG Search](#running-the-rag-search)
- [Project Structure](#project-structure)

## Overview

This project implements a powerful search mechanism using RAG, which combines a retriever model (for fetching relevant documents) and a generator model (for generating answers based on those documents). Pinecone is used to store and manage vectorized representations of documents, allowing fast and scalable similarity search.

### Key Components:

- **Pinecone**: A vector database for efficient storage and similarity search.
- **Retriever**: A model to fetch relevant documents from Pinecone based on a given query.
- **Generator**: A generative model that produces the response by combining the retrieved documents.
- **Python 3.10.11**: The required Python version for running the project.

## Prerequisites

Make sure you have the following installed:

- Python 3.10.11
- Pip (Python's package installer)

You'll also need to set up a Pinecone account and retrieve your API key.

## Installation

1. Clone this repository to your local machine:
   
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

2. Install required dependencies

   ```bash
   pip install -r requirements.txt

## Usage

Setting up Pinecone
1. Create a Pinecone account and get your API key from Pinecone.

## Project Structure

rag-search-project/

├── create_pinecone_index.py # New Pinecone Index  
├── embeddings.py # All embeddings functions      
├── main.py # Stream lit main file     
├── pinecone_service.py # All pinecone services      
├── README.md            
├── requirements.txt # All requirements            
├── utils.py # All helper functions
