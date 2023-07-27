<!-- markdownlint front_matter_title="" -->

# PAIK - Private AI Knowledgebase

ML/AI LLM powered knowledgebase, private algorithms and computation for private/public data.

# Roadmap

## Active

- [ ] Starting with localGPT
  - Inspired by several features of [**localGPT**](<https://github.com/PromtEngineer/localGPT>)

### localGPT notes

- [X] GPU processing is not available; this feature has not been carried over from localGPT. Possibly in the future.
- [X] License: Apache 2.0 (from localGPT)

## Next Feature

- [ ] Integrate PrivateGPT
  - Inspired by several features of [**PrivateGPT**](<https://github.com/imartinez/privateGPT>)

## Future

- Create update of knowledgebase for new source documents
- Organize source docs folder
- Maybe integrate [**langFlow**](<https://github.com/logspace-ai/langflow>)
- Add writing style transfer capability
- Create options to run OpenAI for various ML/AI/chat functions
- Add capability to pull a file via URL
- Add YouTube video summarizer capability; not dependent on transcripts - voice to text to summaries

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

Create new virtual environment by running the command `python3 -m venv paik`.

Activate virtual environment by running the command `source paik/bin/activate`. 

Setting up the execution environment to run the code, start with installing all requirements. Run the command `pip install -r requirements.txt`.

# Running the code

*Note:* The localGPT code defaults to using the GPU. This code base defaults to CPU. The `--device-type` flag is not needed when running this code. 

1. Run the following command `python3 ingest.py` to ingest all the data.

2. Run the following command `python3 run_localGPT.py` to run the code.

3. Type in your questions at the prompt.

## Running the UI

1. Run the following command `python3 run_localGPT_API.py`. The API should being to run.

2. Wait until everything has loaded in. You should see something like `INFO:werkzeug:Press CTRL+C to quit`.

3. Open up a second terminal and activate the same python environment.

4. Navigate to the `/localGPTUI` directory.

5. Run the command `python3 localGPTUI.py`.

6. Open up a web browser and go the address `http://localhost:5111/`.
