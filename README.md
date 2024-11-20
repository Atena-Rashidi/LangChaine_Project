# **Building Interactive ChatBot with Langchain and Streamlit**

**1. Introduction**
   - Brief overview of Langchain and Streamlit
   - Importance of integrating AI models into web applications

**2. Importing Libraries**
   - **Langchain Libraries:**
     - `ChatOpenAI`: For managing chat-based interactions with OpenAI models
     - `ChatPromptTemplate`: For defining and structuring prompts
     - `StrOutputParser`: For parsing string outputs
   - **Streamlit:**
     - For creating interactive web applications
   - **OS Module:**
     - For interacting with the operating system
   - **Dotenv:**
     - For loading environment variables from a `.env` file

**3. Loading Environment Variables**
   - Using `load_dotenv()` to load variables from a `.env` file

**4. Setting Environment Variables**
   - Setting `LANGCHAIN_TRACING_V2` and `LANGCHAIN_API_KEY` from the `.env` file

**5. Creating a Prompt Template**
   - Defining a system message and a user message placeholder for questions

**6. Setting Up Streamlit**
   - Creating a simple web interface with a title and a text input field

**7. Configuring the Language Model**
   - Configuring the Ollama language model (LLama2)
   - Setting up an output parser

**8. Creating a Chain**
   - Combining the prompt template, language model, and output parser to create a chain

**9. Handling User Input**
   - Processing user input through the chain
   - Displaying the result in the web interface


## ----------------------------------------------------------


# **Deploying Large Language Models as APIs with Langchain and FastAPI**

Deploying large language models (LLMs) as APIs using Langchain and FastAPI is a crucial step towards production-grade deployment. 

## **Recap of Previous Work**
In the previous section, the creation of chatbots using both the OpenAI API and open-source LLM models like Llama 2 was explored. Now, let's we move towards deploying these models in a production environment.

## **Objective of This Session**
The main goal is to demonstrate how to create APIs for LLM models, which is essential for efficient deployment. Langserve, a component of Langchain, along with FastAPI, will be used to achieve this. Additionally, a Swagger UI for API documentation, provided by the Langserve library, will be created.

## **Key Components**
1. **Langserve**: This tool helps create and manage API routes.
2. **FastAPI**: A modern web framework for building APIs quickly and efficiently.
3. **Swagger UI**: Automatically generated API documentation that makes it easy to understand and use the APIs.

## **Detailed Steps**
1. **Setting Up the Environment**:
   - Install necessary libraries: Langchain, FastAPI, and Uvicorn.
   - Initialize environment variables, including the OpenAI API key.
2. **Creating the FastAPI Application**:
   - Define the FastAPI app and set up routes for different LLM models.
   - Integrate Langserve to manage these routes.
3. **Defining API Endpoints**:
   - Create endpoints for interacting with OpenAI and Llama 2 models.
   - Use prompt templates to define the tasks for each model.
4. **Running the Application**:
   - Use Uvicorn to run the FastAPI application locally.
   - Access the Swagger UI to view and test the API documentation.

## **Practical Coding Session**
The code will be written step-by-step, ensuring that:
- Necessary libraries are imported.
- Environment variables are initialized.
- The FastAPI app and routes are defined.
- Prompt templates for different tasks are created.
- The application is run and the APIs are tested using Swagger UI.

## **Importance of API Creation**
Creating APIs is crucial for integrating LLM functionalities with various applications, whether they are web, mobile, or desktop apps. This approach allows leveraging multiple LLM models based on their performance metrics and specific needs, ensuring flexibility and efficiency in deployment.

## **Conclusion**
Now, it should be a clear understanding of how to deploy LLMs as APIs using Langchain and FastAPI. This knowledge will enable making these powerful models accessible for various applications in a production environment.


## ----------------------------------------------------------


# **Enhancing Document Querying with a Retrieval-Augmented Generation (RAG) Pipeline Using LangChain and LLMs**

## **Introduction:**
- Focus on the RAG pipeline (Retrieval-Augmented Generation).
- Importance of RAG in using LLM models for querying documents.

## **Overview of RAG:**
- RAG involves querying various data sources.
- Essential for handling different file types (PDF, text, database files, etc.).

## **Components of RAG Pipeline:**
1. **Load Data Source:**
   - Initial step involves loading various file types (PDF, MD, Excel, TXT, database files).
   - Process of importing and loading data from various sources into the system is known as data ingestion.
   - LangChain offers various data ingestion tools.

2. **Data Transformation:**
   - After data ingestion, data is loaded, transformed, and embedded.
   - Loading: Reading from a specific data source.
   - Transformation: Feature engineering and breaking data into smaller chunks.
   - Importance of chunking due to LLM context size limitations.

3. **Embeddings:**
   - Converting data chunks into vectors.
   - Storing vectors in a vector database for efficient querying.
   - Querying the database to retrieve results based on query context.

**Data Ingestion Techniques:**

1. **Reading Text Files:**
   - Use `TextLoader` to read text files.
   - Example: Reading a `speech.txt` file and converting it into text documents.

2. **Environment Variables:**
   - Import necessary libraries (`os`, `dotenv`).
   - Load environment variables, such as API keys, using `load_dotenv`.

3. **Reading from Web Pages:**
   - Use `WebBaseLoader` to read content from web pages.
   - Example: Reading a GitHub page using BeautifulSoup (`bs4`).
   - Steps:
     - Import `WebBaseLoader` and `bs4`.
     - Specify the web path (URL) and parsing arguments.
     - Use `soup_strainer` to filter specific HTML elements (e.g., post title, content, header).
     - Execute the loader to convert web content into text documents.

4. **Reading PDF Files:**
   - Use `PyPDFLoader` to read PDF files.
   - Example: Reading an `attention.pdf` file.
   - Steps:
     - Import `PyPDFLoader`.
     - Specify the PDF file name.
     - Execute the loader to convert PDF content into text documents.

**Transforming Data:**
- **Importance of Transformation:**
  - Convert large documents into smaller, manageable chunks.
  - Essential for handling context size limitations of LLMs.

- **Using Text Splitters:**
  - Example: `RecursiveCharacterTextSplitter` from LangChain.
  - Steps:
    - Define chunk size and overlap.
    - Split documents into smaller chunks.
    - Display the top chunks to verify the transformation.

**Embedding Data:**
- **Vector Embeddings:**
  - Convert text chunks into vectors using embedding techniques.
  - Example: Using OpenAI embeddings.
  - Steps:
    - Import `OpenAIEmbeddings` from LangChain.
    - Create vectors from text chunks.

**Storing Vectors:**
- **Vector Stores:**
  - Store vectors in a database for efficient querying.
  - Example: Using `ChromaDB` as a vector store.
  - Steps:
    - Import `ChromaDB` from LangChain.
    - Create a vector store from documents.
    - Handle dependencies and install necessary libraries (e.g., `ChromaDB`, `FAISS`).

**Querying the Vector Database:**
- **Formulating Queries:**
  - Example query: "Who are the authors of 'Attention is All You Need' research paper?"
  - Use `similarity_search` to retrieve relevant documents from the vector database.
  - Display the results, including author names and other relevant information.

- **Handling Different Queries:**
  - Example: "What is 'Attention is All You Need'?"
  - Retrieve and display relevant content from the vector database.

**Using Alternative Vector Databases:**
- **FAISS Vector Database:**
  - Example: Using `FAISS` as an alternative to `ChromaDB`.
  - Steps:
    - Import `FAISS` from LangChain.
    - Create a vector database (`DB1`) using FAISS.
    - Perform similarity searches and retrieve results.

**Conclusion:**
- **Summary of RAG Pipeline:**
  - Load data from various sources.
  - Transform data into manageable chunks.
  - Embed data into vectors.
  - Store vectors in a vector database.
  - Query the vector database to retrieve relevant results.

## ----------------------------------------------------------

# Advanced RAG Pipeline Using Retriever and Chain Concepts in LangChain

LangChain provides powerful tools for building sophisticated data processing and retrieval systems. Two key components in LangChain are **chains** and **retrievers**. This document explains their definitions, purposes, functionalities, and how they work together.

## Chain
A chain in LangChain refers to a sequence of operations or calls that can include interactions with an LLM (Large Language Model), tools, or data pre-processing steps. Chains automate and streamline processes that involve multiple steps, such as data retrieval, transformation, and querying.
- **Modularity:** Break down complex tasks into smaller, manageable steps.
- **Reusability:** Reuse chains across different projects or parts of your application.
- **Flexibility:** Customize chains to fit specific workflows, making them adaptable to various use cases.

### Example Functions
- **Create Stuff Document Chain:** Takes a list of documents, formats them into a prompt, and passes it to an LLM.
- **Create SQL Query Chain:** Generates SQL queries from natural language inputs.

## Retriever
A retriever in LangChain is an interface designed to fetch documents or data given an unstructured query. It acts as a bridge between the query and the data source, ensuring relevant information is retrieved efficiently. Retrievers handle the initial step of fetching data in response to a query, which can then be processed further by chains or other components.
- **Generalization:** More general than vector stores; they don't need to store documents but only to retrieve them.
- **Efficiency:** Optimize the process of fetching relevant documents from a data source.
- **Integration:** Work with various back-end data stores, including vector stores, to provide the necessary data for further processing.

### Functionality
- **Vector Store Integration:** Use vector stores as their backbone to perform similarity searches and fetch relevant documents.
- **Query Handling:** Process unstructured queries and return the most relevant documents based on the query.

## Combining Chains and Retrievers

In an advanced RAG (Retrieval-Augmented Generation) pipeline, chains and retrievers work together to provide a seamless data processing and retrieval experience:

1. **User Inquiry:** The user submits a query.
2. **Retriever:** The retriever fetches relevant documents from the data source.
3. **Chain:** The chain processes these documents, formats them into a prompt, and sends them to an LLM.
4. **LLM Response:** The LLM generates a response based on the prompt and the retrieved documents.


## 1. Recap of Previous Tutorial
- **Simple RAG Pipeline:**
  - Data sources: PDFs, websites.
  - Data loading using various techniques in LangChain.
  - Transformation of data by breaking down PDFs into chunks.
  - Conversion of chunks into vectors and storing them in a vector store.
  - Querying the vector store to retrieve data.

## 2. Advanced Concepts

### Limitations of Query Vectors
- **Issue:** Query vectors may not retrieve complete results efficiently.
- **Solution:** Use LLM (Large Language Models) for better results.

### Importance of Prompts
- **Role:** Prompts are crucial in the advanced RAG pipeline.
- **Concepts:** Chain and Retriever in LangChain.

## Detailed Explanation

### Chain and Retriever
- **LLM Models:** Use of open-source or OpenAI models.
- **Customization:** Implementation of Chain and Retriever.

### Stuff Document Chain
- **Function:** Takes a list of documents, formats them into a prompt, and passes it to an LLM.
- **Practical Steps:**
  - Reading a PDF and loading documents.
  - Using Recursive Character Text Splitter to convert documents into chunks.
  - Storing chunks in a vector store using embeddings (OpenAI or AMA embeddings).

## 3. Combining Prompts with Chain and Retriever

### Designing a Chat Prompt Template
- **Example Prompt:** "Answer the following question based only on the provided context."
- **LLM Models:** Using models like Llama 2 for generating responses.

## 4. Practical Implementation

### Loading Llama 2 Model
- **Steps:**
  ```python
  from langchain.chains.combine_documents import create_stuff_document_chain
  ```

### Creating a Chain
- **Definition:** A chain refers to a sequence of calls to an LLM, tool, or data pre-processing step.
- **Primary Method:** Using LCL (LangChain Language).

### Functions in Chain
- **Create Stuff Document Chain:** Takes documents from the vector store, formats them into a prompt, and sends them to the LLM.
- **Create SQL Query Chain:** Useful for working with SQL databases for natural language queries.

## 5. Explanation of Retriever

### Definition
- **Retriever:** An interface that retrieves documents given an unstructured query.
- **Functionality:** More general than a vector store; it does not need to store documents, only to return or retrieve them.

### Implementation
- **Code:**
  ```python
  retriever = db.as_retriever()
  ```

### Combining Retriever and Document Chain
- **Process:** The retriever fetches relevant documents from the vector store, which are then passed to the LLM via the document chain to generate responses.

## 6. Creating a Retriever Chain

### Definition
- **Retriever Chain:** Takes a user inquiry, passes it to the retriever to fetch relevant documents, and then to the LLM to generate a response.

### Implementation
- **Code:**
  ```python
  from langchain.chains import create_retrieval_chain

  retrieval_chain = create_retrieval_chain(retriever=retriever, document_chain=document_chain)
  response = retrieval_chain.invoke(input="Your query here")
  ```

### Example Use Case
- **Combining Retriever and Document Chain:** Handling user inquiries and generating responses.

## ----------------------------------------------------------
