"""' Import the ChatOpenAI class from the langchain_openai module
Use case: To create and manage chat-based interactions with OpenAI models

Import the ChatPromptTemplate class from the langchain_core.prompts module
Use case: To define and structure prompts for chat interactions

Import the StrOutputParser class from the langchain_core.output_parsers module
Use case: To parse and handle string outputs from the chat interactions

Import the Streamlit library as st
Use case: To create interactive web applications for data visualization and user interfaces

Import the os module
Use case: To interact with the operating system, such as accessing environment variables

Import the load_dotenv function from the dotenv module
Use case: To load environment variables from a .env file into the application """

# Importing dependencies
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
# Set the OpenAI API key from the environment variable
load_dotenv()  # This will load the variables from the .env file
# Now you can access the API key
API_KEY = os.getenv("OPENAI_API_KEY")
if API_KEY is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")
os.environ["OPENAI_API_KEY"] = API_KEY
# Enable Langchain tracing (version 2) by setting the environment variable to True
os.environ["LANGCHAINE_TRACING_V2"] = "true"
# Set the Langchain API key from the environment variable
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# prompt template
prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant. Please response to the user's query"),
        ("human", "{question}"),
    ]
)


# streamlit Framework
# Set the title of the Streamlit app
st.title("ChatBot with LangChanin and OpenAI")

# Add a description to the app
st.write("This is a simple ChatBot")

# Create a text input box for user queries
input_text = st.text_input("Search your topics:")


# Initialize the GPT-3.5-turbo model with a temperature setting of 0 for deterministic responses
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Initialize the output parser
output_parser = StrOutputParser()

# Chain the prompt, language model, and output parser together
chain = prompt | llm | output_parser

# Check if the user has entered any text
if input_text:
    # Process the user input through the chain and display the response
    st.write(chain.invoke({"Question" + input_text}))
