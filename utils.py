import logging
from langchain.embeddings import HuggingFaceInstructEmbeddings

from langchain.embeddings import OpenAIEmbeddings

from constants import EMBEDDING_MODEL_MAP, EMBEDDING_MODEL_CLASSIFICATION, OPENAI_API_KEY

def create_embeddings(EMBEDDING_MODEL_NAME: str, device_type: str):

    # logging.info("Starting embeddings with model: " + EMBEDDING_MODEL_NAME + ", on: " + device_type)
    
    # Lookup the model name in the embedding model map
    embedding_clasification = EMBEDDING_MODEL_CLASSIFICATION
    embedding_model = EMBEDDING_MODEL_MAP.get(EMBEDDING_MODEL_NAME)
    model_name = embedding_model.get("model_name")
    embedding_family = embedding_model.get("family")

    logging.info("Creating embeddings with, classification: " + embedding_clasification + ", family: " + embedding_family + ", model: " + model_name + ", on: " + device_type)
    
    embeddings = None

    if embedding_family.lower() == "huggingface":
        # Create embeddings
        embeddings = HuggingFaceInstructEmbeddings(
            model_name = model_name,
            model_kwargs = {"device": device_type},
        )
        # change the embedding type here if you are running into issues.
        # These are much smaller embeddings and will work for most appications
        # If you use HuggingFaceEmbeddings, make sure to also use the same in the
        # run_localGPT.py file.

        # embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    elif embedding_family.lower() == "openai":
        
        # Create embeddings
        embeddings = OpenAIEmbeddings(
            model = model_name.split("/")[1],
            openai_api_key = OPENAI_API_KEY,
        )

    return embeddings



def create_and_store_db(texts, embeddings, persist_directory, client_settings):

    # Create the vector store
    db = Chroma.from_documents(
        texts,
        embeddings,
        persist_directory=persist_directory,
        client_settings=client_settings,
    )
    
    return db
