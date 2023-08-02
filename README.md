<!-- markdownlint front_matter_title="" -->

# PAIK - Private AI Knowledgebase

ML/AI LLM powered knowledgebase, private algorithms and computation for private/public data.

## THANK YOUs

[**privateGPT**](<https://github.com/imartinez/privateGPT>)
[**private-chatbot-mpt30b-langchain**](<https://github.com/mayooear/private-chatbot-mpt30b-langchain>)
[**localGPT**](<https://github.com/PromtEngineer/localGPT>)

## Usage Notes

The package python `auto-gptq` has been disabled in the `requirements.txt` file. The `pip install -r requirements.txt` was crashing on the package; maybe it was temporary.

# Roadmap

## Active

- [ ] Update `paik.py` to use the new `utils.py` file
- [ ] Expand options for local/cloud LLMs
  - [ ] Option to use OpenAI GPT-3.5/4 for chat logic processing

## Next Feature

- [ ] Enable classification of data type (private/public) to determine which embeddings and LLM to use. Private data will use only locally executed embeddings (e.g., HuggingFace or other local embeddings) and LLMs. Public data will use be allowed to use (not mandatory) OpenAI and other cloud hosted embeddings and LLMs.

## Future

- [ ] Investigate KnowldgeGRT
  - [ ] Add YouTube video summarizer capability; not dependent on transcripts - voice to text to summaries
  - Add capability to pull a file via URL
- [ ] Add writing style transfer capability
- [ ] Expand options for local/cloud LLMs
- [ ] Options for other free/inexpensive/available LLM APIs, i.e., Anthropic, Llama2, etc.

## Done

*Note:* This is a list of completed tasks. The list roughly in order.

- [X] Create a roadmap
- [X] Starting with localGPT
  - Inspired by several features of [**localGPT**](<https://github.com/PromtEngineer/localGPT>)
  - [X] GPU processing is not available; this feature has not been carried over from localGPT. Possibly in the future.
  - [X] License: Apache 2.0 (from localGPT)
- [X] Create update of knowledgebase for new source documents
  - localGPT has this feature
- [X] Investigate langflow
  - Create options to run OpenAI for various ML/AI/chat functions
  - Conclusion: Langflow is not a good fit for this project. Direct access to the source code of the modules is needed for the openness of the project.
- [ ] Formalizing constants.py
  - [X] Add constant for processor type.  *Note:* The localGPT code defaults to using a GPU. This code base defaults to a CPU. The `--device-type` flag has been moved to an environment variable of `PROCESSOR_TYPE`.
  - [X] Add constant for classification of data type (private/public). 
    - *Note:* This is to be used to determine which embeddings and LLM to use. Private data will use only locally executed embeddings (e.g., HuggingFace or other local embeddings) and LLMs. Public data will use (*future feature* (maybe): be allowed to use) OpenAI and other cloud hosted embeddings and LLMs.
    - *Note:* The code is not in place to use classification of data type.
  - [X] Moved `--device-type` flag to environment variable `PROCESSOR_TYPE`
  - [X] Moved PROCESSOR_MAP to constants.py from run_localGPT.py
  - [X] Created an EMBEDDING_MAP in constants.py to hold the embedding model names, classification, and thier family (e.g., HuggingFace, OpenAI, etc.)
  - [X] Moved the creation of embeddings to the `utils.py` file to improve code reuse around swapping out embeddings and LLMs
  - [X] Moved the creation of the local Chroma db to the `utils.py` file to improve code reuse in the future. There is no functionality change.
- [X] Provide option to reduce local workload of content is not private
  - [X] Option to use OpenAI ADA for embeddings
  - *Note:* The structure established to enable local(private) vs cloud(public) processing is in place for other embeddings, vector DBs, and LLMs. The code is in place to use optional embeddings only.

# Contributing

- Be nice
- Drop me a message somehow (via GitHub maybe?) :)
- Do some git stuff in the repo; I'll likely notice

# Paik (the word)

[Merriam-Webster](<https://www.merriam-webster.com/dictionary/paik>)

  ```text
    paik
    transitive verb
    ˈpāk
    -ed/-ing/-s
    dialectal, British
    : to strike hard and repeatedly : pummel
  ```

and... sometimes i feel like pummeling my head against the keyboard... the fun part is when the code pummels the work ```;)```

# Environment Setup

Install python venv by running the command `pip install virtualenv`.

Create new virtual environment by running the command `python3 -m venv venv-paik`.

Activate virtual environment by running the command `source venv-paik/bin/activate`. 

Setting up the execution environment to run the code, start with installing all requirements. Run the command `pip install -r requirements.txt`.

# Running the code

1. Run the following command `python3 ingest.py` to ingest all the data.

2. Run the following command `python3 run_localGPT.py` to run the code.

3. Type in your questions at the prompt.
