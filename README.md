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
- [Sample Outputs](#sample-output)

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

## Sample Outputs
1. Query -It's just the obsessive questions for unrelated things that she
	Output - Oh, I think it's just she's just draining. It's just the obsessive questions for unrelated things that she doesn't understand how it gets built. So it's like, she's like dealing with my apprentice, having to explain everything to her every step of the way. even all my subies are getting sick of it too, because they're like they're asking, she's asking us how are we going to do that, how we do this and why we're doing this and why we're doing that. And they're like, well, this isn't our first radio, we've been doing this for 20 years, we know how to connect up wires, we know how to do this. 3:54 - Coach Yeah, what's what I'm what's my name? The reason I'm asking will become a parent soon. 3:58 - Client 001 Yeah, highly. 4:00 - Coach H-A-Y-L-E-Y, I'm Okay, yeah, early while, yeah. Yeah. So she's asking many questions writing to the job. What's, to be annoying as a business coach, to make sure I get the right info here. What's wrong with that? Why is that ticking off?

2. Query - Yeah, I've written that down. 
	Yeah Because then she'll come to meet me like I've youtube this and this is how they say it's done Yeah Feel like whacking the phone out of a hand and throwing it across the room Yeah, I'm not an aggressive person I get it that would be frustrating All right, so I'll just talk some notes there and type that in as if I can spell in the chat tpt uh so that's question one question two What boundaries have you set if any regarding communication with clients? How do you typically prioritize or respond to time-consuming queries? 8:54 - Client 001 Have any specific boundaries Yeah, look normally if someone's trying to call me at like five or something something. I just sent a text message. Sorry, I can't answer the call right now. I'm spending, you know, I've clocked off for the day and it is now family time. Please, you know, send me an email or give me a call first thing tomorrow. Okay, perfect. But yeah. 9:21 - Coach