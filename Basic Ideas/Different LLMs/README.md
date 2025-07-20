## The Cast of LLM Characters

These are the key LLM providers we will encounter during agentic AI development:

- **OpenAI**: gpt-4o-mini (also gpt-4o, o1, o3-mini)
- **Anthropic**: Claude-3-7-Sonnet
- **Google**: Gemini-2.0-Flash
- **DeepSeek AI**: DeepSeek V3, DeepSeek R1
- **Groq**: Open-source LLMs incl. Llama3.3
- **Ollama**: Local open-source LLMs incl. Llama3.2

For comparison of cost, speed, and performance, check:
[ `https://www.vellum.ai/llm-leaderboard` ](Vellum Leaderboard)

---

## 🌐 What Is the OpenAI API?
The OpenAI library is lightweight — it is not an LLM or neural network itself.

It simply wraps HTTP calls to a standard API format.

We send structured requests (like lists of dictionaries) to OpenAI’s endpoints.
Many other providers now follow this same format, making it easy to swap models.

---

## Why We Use OpenAI Code to Call Gemini

Simple — the OpenAI Python client just sends HTTP requests using a common API format.

Since OpenAI's API format became widely adopted, many providers (like Gemini) support the same structure.









