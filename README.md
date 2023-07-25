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

and... sometimes i feel like pummeling my head against the keyboard... the fun part is when the code works ```;)```

# Environment Setup

Install python venv

  ```shell
  pip install virtualenv
  ```

Create new virtual environment

  ```shell
  python3 -m venv paik
  ```

Activate virtual environment

  ```shell
  source paik/bin/activate
  ```

In order to set your environment up to run the code here, first install all requirements:

  ```shell
  pip install -r requirements.txt
  ```

# Running the code

*Note:* The localGPT code defaults to using the GPU. This code base defaults to CPU. The `--device-type` flag is not needed when running this code. 

Run the following command to ingest all the data.

  ```shell
  python3 ingest.py
  ```

Run the following command to run the code.
  
  ```shell
  python3 run_localGPT.py
  ```
