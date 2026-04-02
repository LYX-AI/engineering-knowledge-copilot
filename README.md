# Engineering Knowledge Copilot

## Project Overview
Engineering Knowledge Copilot is a local, minimal RAG-based knowledge assistant project.

Its purpose is to help users ask questions about engineering and testing documents, and get answers grounded in retrieved documentation.

This project is also the foundation for a later extension: a test failure triage agent.

---

## Why I am building this
I am building this project as part of my transition from software test automation into an AI/LLM application role.

The goal is not to build a full enterprise product at the beginning.
The goal is to create a clear, runnable, and explainable project that demonstrates:

- RAG pipeline understanding
- vector database usage
- LLM application design
- engineering-oriented AI problem solving

---

## Current Scope (Phase 1)
This phase only focuses on a minimal local version:

- local documents only
- text-based knowledge base
- command-line question answering
- simple retrieval + answer generation
- no UI
- no cloud deployment
- no agent workflow yet

---

## Planned Pipeline
The first version of the system will follow this pipeline:

Document -> Chunking -> Embedding -> Vector Store -> Retrieval -> LLM Answer

Later, this project will be extended into:

Log Input -> Agent Analysis -> Knowledge Retrieval -> Suggested Root Causes

---

## Initial Documents
The first version uses three small example documents:

- `test_runbook.txt`
- `common_errors.txt`
- `faq.txt`

These documents simulate engineering/testing knowledge and are only used to validate the first working version of the pipeline.

---

## Project Goal for Day 1
By the end of Day 1, I should have:

- the project structure created
- the README initialized
- three sample documents prepared
- a clear definition of the project scope

---

## Next Step
The next implementation step is:

- install dependencies
- prepare the local environment
- write `ingest.py`
- start loading and chunking documents
