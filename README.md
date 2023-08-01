<!-- markdownlint front_matter_title="" -->

# PAIK - Private AI Knowledgebase

ML/AI LLM powered knowledgebase, private algorithms and computation for private/public data.

# Roadmap

## Active

- [X] Flip to privateGPT as a codebase
  - privateGPT is being used now, instead of localGPT, due to much less code to work with and modify in the short-term.
  - A web-based UI is desired, which will likely be built with Streamlit. localGPT is the inspriation for this, but is built in Flask and is not as easy to modify.
  - Must manually create local 'models' directory and download hardcoded models
- - Updates:
    - [X] Renamed `privateGPT.py` to `paik.py`
    - [ ] Update `constants.py` and usage to consolidate settings
      - Thank you 

## Next Feature

- [ ] Provide option to reduce local workload of content is not private
  - [ ] Option to use OpenAI ADA for embeddings
  - [ ] Option to use OpenAI GPT-3.5/4 for chat logic processing
  - [ ] Options for other free/inexpensive/available LLM APIs

## Future

- Investigate KnowldgeGRT
  - Add YouTube video summarizer capability; not dependent on transcripts - voice to text to summaries
  - Add capability to pull a file via URL
- Add writing style transfer capability

## Done

- [X] Create a roadmap
- [X] Starting with localGPT
  - Inspired by several features of [**localGPT**](<https://github.com/PromtEngineer/localGPT>)
- [X] Create update of knowledgebase for new source documents
  - localGPT has this feature
- [X] Investigate langflow
  - Create options to run OpenAI for various ML/AI/chat functions
  - Environment variable on MacOS `OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES` must be set to `YES` to run langflow
  - Conclusion: Langflow is not a good fit for this project. Direct access to the source code of the modules is needed for the openness of the project.

### localGPT notes

- [X] GPU processing is not available; this feature has not been carried over from localGPT. Possibly in the future.
- [X] License: Apache 2.0 (from localGPT)

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
