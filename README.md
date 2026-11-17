# LangGraph Task Agent

A tool-calling agent built with [LangGraph](https://langchain-ai.github.io/langgraph/).
The graph lives in `src/agent/graph.py`; tools are in `src/agent/tools.py`.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # add your OpenAI key
```

## Run

```bash
python -m agent "What is 17% of 2,340?"
# or with LangGraph Studio / dev server
langgraph dev
```

## Test

```bash
pytest
```
