
import streamlit as st  # Web framework for building interactive apps
# Load documents from various formats
from langchain.document_loaders import YoutubeLoader
# Split text into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Generate embeddings using OpenAI API
from langchain_openai import OpenAIEmbeddings
# Store and retrieve vectors efficiently
from langchain.vectorstores import FAISS
# Create conversational chains
from langchain.chains import RetrievalQA, RetrievalQAWithSourcesChain
# Use ChatOpenAI LLM for conversations
from langchain_openai import ChatOpenAI
# Access OpenAI API
import openai
# get environment

# import prompt template from templates file
from prompts_template import PROMPT

import os
from typing import List, Union
import langdetect


def get_api_key() -> str:
    """
    The user has two options, use env or input the key on the browser.
    Try to get the Open API key from env.
    Prompts the user for their OpenAI API key and validates it.

    Returns:
        str: The validated OpenAI API key or None if invalid.
    """

    env_api_key = os.getenv('OPENAI_API_KEY')
    # Create a text input for the user to enter their API key
    open_api_key = st.text_input(
        label="OpenAI API Key",
        placeholder="Ex: sk-2twmA8tfCb8un4...",
        key="openai_api_key_input",
    )

    # check option to use env or input in the browser
    if not open_api_key and env_api_key:
        open_api_key = env_api_key

    # Check if the entered API key starts with "sk-" (a valid OpenAI API key format)
    if not open_api_key.startswith("sk-"):
        return None  # Return None if the API key is not valid

    return open_api_key  # Return the validated API key


def process_video_data(url: str) -> Union[str, dict]:
    """Processes uploaded video transcript.

    Args:
        url: A Youtube video url.

    Returns:
        transcript: A String of the video transcript.
        metadata: A dictionary of the video metadata    
    """
    try:
        loader = YoutubeLoader.from_youtube_url(
            url,
            language=["en", "ar"],
            add_video_info=True,)

        Video_data = loader.load()

        transcript, metadata = Video_data[0].page_content, Video_data[0].metadata

        return transcript, metadata
    except Exception as e:
        st.error(e)
        st.stop()

def split_transcript_chunks(transcript: str) -> list:
    """Splits a transcript text into smaller chunks for efficient processing.

    Args:
        transcript: A String of video transcript.

    Returns:
        list: A list of smaller chunks.
    """
    # Create a text splitter object with specific chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=400,
        length_function=len,
    )

    # Split the transcript into smaller chunks
    chunks = text_splitter.split_text(transcript)

    return chunks  # Return the list of smaller chunks


def get_vectorstoredb(
        chunks: list, open_api_key: str) -> FAISS:  # Specify return type for clarity
    """Creates a vector store database for the chunks using OpenAI embeddings.

    Args:
        chunks: A list of processed documents.
        open_api_key: The OpenAI API key.

    Returns:
        FAISS: The created vector store.
    """
    try:
        # Create an object to generate text embeddings using the OpenAI API
        embeddings = OpenAIEmbeddings(api_key=open_api_key)

        # Build the vector store using the chunks and embeddings
        # Create a FAISS instance for vector database from 'data'
        vectorstore_db = FAISS.from_texts(texts=chunks,
                                          embedding=embeddings)


        return vectorstore_db  # Return the built vector store

    except openai.APIError as e:
        # Handle any errors from the OpenAI API
        print(f"OpenAI API returned an API Error: {e}")
        st.warning(f"OpenAI API returned an API Error: {e}")
        st.stop()  # Stop the Streamlit app if an error occurs


def get_qa_chain(vectorstore_db, open_api_key):
    """
    Creates a RetrievalQA chain, combining a large language model (LLM) with the vector store.

    Args:
        vectorstore: The vector store containing processed documents.
        open_api_key: The user's OpenAI API key for accessing the LLM.

    Returns:
        chain: The created RetrievalQA chain, ready for interaction.
    """

    try:
        chain_type_kwargs = {"prompt": PROMPT}

        llm = ChatOpenAI(model_name="gpt-3.5-turbo", 
                         temperature=0, api_key=open_api_key
                         )

        
        # this is much faster
        chain = RetrievalQA.from_chain_type(llm=llm,
                                            chain_type="stuff",
                                            retriever=vectorstore_db.as_retriever(),
                                            input_key="query",
                                            chain_type_kwargs=chain_type_kwargs)

        return chain  # Return the created RetrievalQA chain

    except openai.APIError as e:
        # Handle any errors from the OpenAI API
        print(f"OpenAI API returned an API Error: {e}")
        st.warning(f"OpenAI API returned an API Error: {e}")
        st.stop()  # Stop the Streamlit app if an error occurs


def handle_userinput(prompt):
    """
    Handles user input and generates a response using the conversational chain.

    Args:
        prompt: The user's input text.
    """

    try:
        # Display the user's input in the chat interface
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the conversational chain
        with st.chat_message("assistant"):
            message_placeholder = st.empty()  # Create a placeholder for the response
            response = ""

            # Get the response from the conversational chain, pass empty chat history, it is required.
            response = st.session_state.qa_chain({"query": prompt})
            result = response["result"]
            
            response = f"**{response['result']}**"  # Format the response

            # Display the response in the chat interface
            message_placeholder.markdown(response, unsafe_allow_html=True)

            # Store the response in the conversation history
            st.session_state.messages.append(
                {"role": "assistant", "content": response})

    # handle any error with open ai key
    except openai.APIError as e:
        # Handle any errors from the OpenAI API
        # print(f"OpenAI API returned an API Error: {e}")
        st.warning(f"OpenAI API returned an API Error: {e}")
        st.stop()
