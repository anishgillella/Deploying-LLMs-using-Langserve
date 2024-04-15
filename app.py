# Import necessary libraries
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI  # Verify the import path is correct for your setup
from langserve import add_routes  # This utility adds routes to a FastAPI application
import uvicorn  # ASGI server for running FastAPI
import os  # Library to interact with the operating system

# Set the API key for OpenAI in the environment variables
api_key = 'your_openai_api_key_here'
os.environ['OPENAI_API_KEY'] = api_key

# Initialize FastAPI app with metadata
app = FastAPI(
    title="Langchain Server",  # Title of the API server
    version="1.0",  # Version of the API
    description="A simple API Server to deploy LLM"  # Short description of what the API server does
)

# Create an instance of ChatOpenAI with default prompt settings
chat_model = ChatOpenAI()
# Add a route to handle general chat model requests
add_routes(
    app,
    chat_model,
    path="/openai"
)

# Define specific prompt templates for different types of content
essay_prompt = ChatPromptTemplate.from_template("provide me an essay about {topic}")
poem_prompt = ChatPromptTemplate.from_template("provide me a poem about {topic}")

# Create ChatOpenAI models with specific prompts for generating essays and poems
model_essay = ChatOpenAI(prompt=essay_prompt)
model_poem = ChatOpenAI(prompt=poem_prompt)

# Add routes for the essay and poem generation endpoints
add_routes(
    app,
    model_essay,
    path="/essay"
)
add_routes(
    app,
    model_poem,
    path="/poem"
)

# Start the FastAPI app using uvicorn with specified host and port
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
