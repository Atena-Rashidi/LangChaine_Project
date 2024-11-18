"""
- from fastapi import FastAPI
This line imports the FastAPI class from the fastapi module. This class is used to create a FastAPI 
application instance, which serves as the main entry point for defining API routes and handling HTTP
requests.

- from langchain.prompts import ChatPromptTemplate:
ChatPromptTemplate is used to create templates for chat prompts, which can be customized and used to
generate specific responses from language models.

- from langchain.chat_models import ChatOpenAI:
ChatOpenAI provides an interface to interact with OpenAI’s chat models, allowing you to send prompts
and receive responses.

- from langserve import add_routes:
add_routes is used to add API routes to a FastAPI application, enabling the integration of different
language models and their functionalities into the API.

- import uvicorn:
uvicorn is an ASGI server for Python web applications. It is used to run FastAPI applications, 
allowing them to handle HTTP requests.

- import os:
The os module provides a way to interact with the operating system, commonly used to access 
environment variables, file paths, and other system-level operations.

- from langchain_community.llms import Ollama:
Ollama represents a specific large language model (LLM) that can be used within the Langchain
framework, allowing for interactions with the Ollama model.

- from dotenv import load_dotenv:
load_dotenv is used to load environment variables from a .env file into the application’s
environment, useful for managing configuration settings like API keys.

"""

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama


from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


"""

- app = FastAPI(...):
  This initializes a new FastAPI application and assigns it to the variable app.

- title="LangChain Server":
 This sets the title of the API documentation to “LangChain Server”. This title will appear in
the automatically generated API documentation (e.g., Swagger UI).

 - version="1.0":
 This specifies the version of the API. In this case, it is set to “1.0”. This version information
 will also be displayed in the API documentation.
 
 - description="A simple API server using LangChain's Runnable interfaces":
 This provides a brief description of the API. It explains that the server is a simple API server
 utilizing LangChain’s Runnable interfaces. This description will be shown in the API documentation
 to give users an overview of the API’s purpose.

 """

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)


"""
Defining two models, such as the OpenAI LLM Model and the Open Source Ollama Model, is particularly
useful for an API because it provides flexibility and versatility in handling different types of requests.
"""

# 1. OpenAI LLM Model
openai_llm = ChatOpenAI()
# 2. Open Source Ollama Model
ollama_llm = Ollama(model="llama2")


prompt_openai = ChatPromptTemplate.from_template("{topic}")
prompt_ollama = ChatPromptTemplate.from_template("{topic}")


"""
By adding these routes, your API will be able to handle requests for both the OpenAI and Ollama models, 
providing flexibility and versatility in handling different types of language model interactions.
"""

# Add a new route for the Ollama model
add_routes(
    app,
    prompt_openai | openai_llm,
    path="/OpenAI",
)

add_routes(
    app,
    prompt_ollama | ollama_llm,
    path="/Ollama",
)


"""
This code snippet is used to run the FastAPI application using Uvicorn, an ASGI server for Python web applications.
When you run this script, it will start the FastAPI application on localhost at port 8000,
making it accessible at http://localhost:8000. This is useful for local development and testing.
"""

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
