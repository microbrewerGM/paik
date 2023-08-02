import os
from chromadb.config import Settings

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Processor map
PROCESSOR_TYPE = os.getenv("PROCESSOR_TYPE", "cpu")
PROCESSOR_MAP = {
    "cpu": "cpu",
    "cuda": "cuda",
    "ipu": "ipu",
    "xpu": "xpu",
    "mkldnn": "mkldnn",
    "opengl": "opengl",
    "opencl": "opencl",
    "ideep": "ideep",
    "hip": "hip",
    "ve": "ve",
    "fpga": "fpga",
    "ort": "ort",
    "xla": "xla",
    "lazy": "lazy",
    "vulkan": "vulkan",
    "mps": "mps",
    "meta": "meta",
    "hpu": "hpu",
    "mtia": "mtia",
}

# https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/excel.html?highlight=xlsx#microsoft-excel
from langchain.document_loaders import CSVLoader, PDFMinerLoader, TextLoader, UnstructuredExcelLoader, Docx2txtLoader

ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

DOCUMENTS_DIRECTORY = os.getenv("DOCUMENTS_DIRECTORY", "SOURCE_DOCUMENTS")
SOURCE_DIRECTORY = f"{ROOT_DIRECTORY}/{DOCUMENTS_DIRECTORY}"

# Define the folder for storing database
PERSISTANCE_DIRECTORY = os.getenv("PERSISTANCE_DIRECTORY", "DB")
PERSIST_DIRECTORY = f"{ROOT_DIRECTORY}/{PERSISTANCE_DIRECTORY}"

# Can be changed to a specific number
INGEST_THREADS = os.cpu_count() or 8


# Define classification of models to be used
# private: models that are executed/ran locally on your machine
# hosted: models that are hosted on a cloud service
EMBEDDING_MODEL_CLASSIFICATION = os.getenv("EMBEDDING_MODEL_CLASSIFICATION", "private")

EMBEDDING_MODEL_MAP = {
    "hkunlp/instructor-large": {
        "model_name": "hkunlp/instructor-large",
        "classfication": "private",
        "family": "HuggingFace"
    },
    "sentence-transformers/all-MiniLM-L6-v2": {
        "model_name": "sentence-transformers/all-MiniLM-L6-v2",
        "classfication": "hosted",
        "family": "HuggingFace"
    },
    "openai/text-embedding-ada-002": {
        "model_name": "openai/text-embedding-ada-002",
        "classfication": "hosted",
        "family": "OpenAI"
    }
}

# You can also choose a smaller model, don't forget to change HuggingFaceInstructEmbeddings
# to HuggingFaceEmbeddings in both ingest.py and run_localGPT.py
# EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Load model and default
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2")
# EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "openai/text-embedding-ada-002")

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
    chroma_db_impl="duckdb+parquet", persist_directory=PERSIST_DIRECTORY, anonymized_telemetry=False
)


# https://python.langchain.com/en/latest/_modules/langchain/document_loaders/excel.html#UnstructuredExcelLoader
DOCUMENT_MAP = {
    ".txt": TextLoader,
    ".md": TextLoader,
    ".py": TextLoader,
    ".pdf": PDFMinerLoader,
    ".csv": CSVLoader,
    ".xls": UnstructuredExcelLoader,
    ".xlxs": UnstructuredExcelLoader,
    ".docx": Docx2txtLoader,
    ".doc": Docx2txtLoader,
}


