# Import the requests library for making HTTP requests
import requests

# Import the Streamlit library for creating web apps
import streamlit as st


# Define a function to get a response from the OpenAI API
def get_openai_response(input_text):
    # Send a POST request to the OpenAI endpoint with the input text
    response = requests.post(
        "http://localhost:8000/OpenAI",  # The URL of the OpenAI API endpoint
        json={"input": {"topic": input_text}},  # The payload containing the input text
    )
    # Return the JSON response from the API
    return response.json()


# Define a function to get a response from the Ollama API
def get_ollama_response(input_text):
    # Send a POST request to the Ollama endpoint with the input text
    response = requests.post(
        "http://localhost:8000/Ollama",  # The URL of the Ollama API endpoint
        json={"input": {"topic": input_text}},  # The payload containing the input text
    )
    # Return the JSON response from the API
    return response.json()


# Set the title of the Streamlit app
st.title("Deploying LLMs as API with LangChain and FastAPI")

# Create a text input field for the OpenAI model
input_text_openai = st.text_input("Search your topic for OpenAI:")

# Create a text input field for the Ollama model
input_text_ollama = st.text_input("Search your topic for Ollama:")

# If there is input for the OpenAI model, display the response
if input_text_openai:
    # Display the response from the OpenAI API
    st.write(get_openai_response(input_text_openai))

# If there is input for the Ollama model, display the response
if input_text_ollama:
    # Display the response from the Ollama API
    st.write(get_ollama_response(input_text_ollama))
