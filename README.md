# LangChain Learning Repository

A practical collection of LangChain and LangGraph-style building blocks for learning how prompts, models, chains, runnables, output parsers, embeddings, and structured responses fit together.

The examples use multiple model providers, including Google Gemini, OpenAI, Anthropic, and Hugging Face. Most scripts are intentionally small and executable so that each LangChain concept can be studied in isolation.

Repository: [github.com/Dipansh631/generative-AI](https://github.com/Dipansh631/generative-AI)

## What This Repository Covers

- Basic LLM and chat-model calls
- Prompt templates and reusable prompt files
- Sequential, parallel, conditional, and branching chains
- LangChain Expression Language and runnable composition
- `RunnableSequence`, `RunnableParallel`, `RunnablePassthrough`, `RunnableLambda`, and `RunnableBranch`
- String, JSON, Pydantic, and structured output parsing
- Pydantic models, `TypedDict`, and annotated schemas
- Text embeddings and semantic search
- OpenAI, Gemini, Anthropic, and Hugging Face integrations
- Streamlit prompt interfaces and a research-paper summarization tool
- A Python 3.11 development-container configuration

## Project Layout

### `chains/`

Examples of classic chain composition and common execution patterns.

- `simplechain.py` - Minimal prompt-to-model-to-output flow.
- `sequentialchain.py` - Runs multiple operations in order, passing each result to the next step.
- `parallelchain.py` - Executes independent prompt/model branches in parallel.
- `conditionalchain.py` - Selects a chain based on a condition.

### `Runnables/`

Focused examples of LangChain Core runnable primitives.

- `runnable_sequence.py` - Composes multiple runnable steps into a sequential pipeline.
- `runnable_parallel.py` - Produces multiple outputs from the same input at the same time.
- `runnable_passthrough.py` - Keeps the original value available while composing runnable branches.
- `Runnable_lambda.py` - Uses `RunnableLambda` to turn a normal Python function into a runnable. The example counts the words in a generated joke.
- `Runnable_branch.py` - Uses `RunnableBranch` to summarize a long generated report while returning shorter reports unchanged.

### `chatmodel/`

Small provider-specific chat-model examples.

- `chatmodel_gemini.py` - Calls Google Gemini through `ChatGoogleGenerativeAI`.
- `chatmodel_openai.py` - Calls an OpenAI chat model.

### `langchain_models/`

A broader set of model and embedding demonstrations.

- `chatmodel/chatmodel_gemini.py` - Gemini chat-model usage.
- `chatmodel/chatmodel_openai.py` - OpenAI chat-model usage.
- `chatmodel/chatmodel_antrophic.py` - Anthropic chat-model usage. The filename preserves the original spelling.
- `chatmodel/chatmodel_hf.py` - Hugging Face model integration.
- `LLMS/llm_demo.py` - Basic LLM demonstration.
- `embedding models/embedding_doc.py` - Embedding documents for retrieval workflows.
- `embedding models/embedding_gemini_query.py` - Gemini-based query embeddings.
- `embedding models/embedding_hf.py` - Hugging Face embedding usage.
- `embedding models/sementic_search.py` - Semantic search using Gemini embeddings and cosine similarity. The filename preserves the original spelling of "semantic".

### `embedding models/`

- `sementic_search.py` - A compact semantic-search example using document and query vectors.

### `LLMS/`

- `llm_demo.py` - Basic language-model demonstration.

### `langchain_prompt/`

Prompt templates, message handling, prompt files, and Streamlit interfaces.

- `chatbot.py` - Chatbot-style prompt and model interaction.
- `chatprompt_template.py` - Chat prompt template examples.
- `message_placeholder.py` - Demonstrates placeholder messages in prompts.
- `messages.py` - Works with LangChain message objects and chat history.
- `chat_history.txt` - Example conversation history data.
- `prompt_generator.py` - Streamlit prompt-generation interface.
- `prompt_ui.py` - Streamlit prompt interface.
- `dynamic_prompt_ui.py` - Streamlit research-paper summarization tool with selectable paper, style, and response length.
- `template.json` - JSON prompt template loaded by `dynamic_prompt_ui.py`.

### `Output_parsers/`

Examples of converting model responses into useful application data.

- `stroutputparser.py` - Parses a model response as a string.
- `jsonoutputparser.py` - Parses model output as JSON.
- `pydanticoutputparser.py` - Parses model output into a Pydantic model.
- `structuredoutputparsers.py` - Demonstrates structured output parser patterns.

### `structured_output/`

Schema-driven output examples using Python typing and Pydantic.

- `pydantic_demo.py` - Validates a student record with Pydantic, including email and CGPA constraints.
- `annonated.py` - Demonstrates annotated structured fields. The filename preserves the original spelling.
- `typeddict_demo.py` - Uses a `TypedDict` schema for structured data.
- `pydantic_structured_output_typedict.py` - Compares or combines Pydantic and `TypedDict` structured output approaches.
- `with_structured_output_json.py` - Requests structured JSON output from a chat model.
- `with_structured_output_typeddict.py` - Requests output shaped by a `TypedDict` schema.

### `help/`

- `test.py` - Small supporting or experimental test script.

### Root files

- `requirements.txt` - Python dependencies for LangChain, provider integrations, embeddings, validation, and supporting utilities.
- `json_schema.json` - JSON schema used by structured-output examples or experiments.
- `.devcontainer/devcontainer.json` - Python 3.11 development-container configuration with Python and Pylance extensions.
- `.gitignore` - Keeps `.env`, `.venv`, and `.vscode` out of version control.

## Requirements

- Python 3.11 or newer is recommended.
- A provider API key for the examples you want to run.
- Internet access for model and embedding API calls.
- Streamlit is required for the UI examples. The devcontainer installs it automatically; local environments should install it separately if it is not already available.

## Installation

### Windows PowerShell

```powershell
git clone https://github.com/Dipansh631/generative-AI.git
Set-Location generative-AI

py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install streamlit
```

### Linux or macOS

```bash
git clone https://github.com/Dipansh631/generative-AI.git
cd generative-AI

python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install streamlit
```

## Environment Variables

Create a local `.env` file in the repository root. Never commit it; `.env` is ignored by Git.

Use only the keys required by the provider or example you are running:

```dotenv
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

The examples call `load_dotenv()` so these values are loaded automatically when the script starts. Do not paste real keys into source files, notebooks, screenshots, commits, or public posts.

## Running Examples

Run scripts from the repository root with the activated virtual environment:

```powershell
python .\chains\simplechain.py
python .\Runnables\Runnable_lambda.py
python .\Runnables\Runnable_branch.py
python .\Output_parsers\jsonoutputparser.py
python .\structured_output\pydantic_demo.py
```

The runnable examples demonstrate the main data-flow patterns:

```text
input dictionary
    -> prompt template
    -> chat model
    -> output parser
    -> runnable sequence / parallel branch
    -> final result
```

For provider-backed examples, the relevant API key must be available in `.env`. Model availability can change over time, so update the model identifier in the example if the provider reports that a model has been retired, renamed, or restricted.

## Running the Streamlit UI

The main interactive research tool is:

```powershell
streamlit run .\langchain_prompt\dynamic_prompt_ui.py
```

It provides controls for:

- Selecting a research paper topic
- Selecting an explanation style
- Selecting a response length
- Sending those choices through the JSON prompt template
- Displaying the cleaned model response in the browser

Other Streamlit interfaces can be started the same way:

```powershell
streamlit run .\langchain_prompt\prompt_ui.py
streamlit run .\langchain_prompt\prompt_generator.py
```

Streamlit normally serves the application at `http://localhost:8501`.

## Dev Container

The repository includes a `.devcontainer/devcontainer.json` based on:

```text
mcr.microsoft.com/devcontainers/python:1-3.11-bookworm
```

It configures the Python and Pylance VS Code extensions, forwards port `8501`, installs `requirements.txt`, and starts the Streamlit application when the container is attached. The local command above is the reliable command when working directly from the repository root.

## Learning Path

A useful order for exploring the repository is:

1. Start with `chains/simplechain.py` to understand prompt, model, and parser composition.
2. Compare `sequentialchain.py` and `parallelchain.py` to see sequential versus concurrent execution.
3. Read the files in `Runnables/` to understand how values move between runnable steps.
4. Explore `Output_parsers/` to convert free-form responses into application data.
5. Use `structured_output/` to add validation and explicit schemas.
6. Try the provider-specific files in `chatmodel/` and `langchain_models/`.
7. Run `langchain_prompt/dynamic_prompt_ui.py` to combine prompts, models, and a user interface.

## Notes and Limitations

- These are educational examples rather than a single production application.
- Several scripts call external APIs immediately when executed.
- API costs, rate limits, authentication, and model availability are controlled by each provider.
- Some filenames intentionally retain their original spelling, including `sementic_search.py`, `annonated.py`, and `chatmodel_antrophic.py`.
- Some examples use hard-coded local paths or model identifiers and may need small adjustments on another machine.
- The repository does not include `.env`, `.venv`, or `.vscode`; each developer creates their own local environment.

## License

No license file is currently included. Add a license before distributing this repository as a reusable library or application.
