# Deep Research Biotech Agent

An end-to-end LLM-powered multi-agent pipeline for automated literature review and insight synthesis in biotech (e.g., antibody therapeutics use case).  
It combines clarification, contextualization, planning, retrieval (PubMed + web), semantic relevance filtering (RAG-style via FAISS), report generation, and stakeholder delivery.

## Features
- Multi-agent prompt chaining: Clarifier → Contextualizer → Planner → Searcher → Optimizer → Writer → Email  
- Live scientific retrieval from PubMed (via Biopython Entrez) + open-web search fallback  
- Semantic relevance filtering using embeddings + FAISS to prune noise  
- Report synthesis grounded in retrieved evidence using OpenAI LLMs  
- Human-in-the-loop query refinement via Gradio UI  
- Automated HTML report delivery via SendGrid  
- Observability: tracing (OpenAI Traces / Langfuse), latency & relevance metrics logged per run  
- Async orchestration for parallel search execution

## Quickstart

### 1. Prerequisites
- Python 3.10+  
- `git` (to clone repo)  
- Internet access (for OpenAI, PubMed, SendGrid)

### 2. Clone and setup
```bash
git clone <your-repo-url>
cd <repo-directory>
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the app (Gradio UI)
```bash
uv ru
