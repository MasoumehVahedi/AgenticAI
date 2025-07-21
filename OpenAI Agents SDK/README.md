## Async I/O: The Agent SDK Backbone

Python’s **asynchronous I/O** is the core concurrency model underpinning every modern agent framework.

### Why async I/O?
- **Lightweight concurrency** without OS threads or multiple processes.  
- **Event loop** swaps between coroutines whenever one is waiting on I/O (e.g., a network/API call).  
- **Scales** to thousands of concurrent tasks with minimal overhead.

- **Basic rules to get started**  
  1. **Define** an async function with `async def`:  
     ```python
     async def fetch_data(url):
         …  
     ```  
  2. **Run** it by awaiting its result:  
     ```python
     data = await fetch_data(url)
     ```  
  3. **Group** multiple coroutines with `asyncio.gather(...)` to run them concurrently.

- **Why it matters for agents**  
  Agents often fan out dozens of API requests at once. Async I/O lets us manage thousands of such calls efficiently—no extra OS threads or processes required.

---

## Minimal Terminology

- **Agent**  
  A lightweight wrapper around LLM calls that encapsulates a particular role or purpose in your system.

- **Handoff**  
  Any interaction or message exchange between two agents.

- **Guardrail**  
  A check or constraint you place around an agent to keep it on‑task and prevent it from “going off the rails.”

---

## Running an Agent: 3 Simple Steps

1. **Create an Agent instance**  
   Configure your LLM, role, and any initial settings.

2. **Wrap with a trace**  
   ```python
   with trace() as session:
       …
  ```

3. **Execute the Agent**
   ```python
   result = await runner.run()
       …
  ```
Run the agent’s main coroutine and await its output.


## Vibe Coding: A Survival Guide

“Vibe coding” is an ad‑hoc, iterative style of working with LLMs: you let the model generate, you tweak, and you iterate—making rapid progress on unfamiliar APIs or large codebases. To keep things smooth and avoid frustrating dead‑ends, follow these five rules:

1. **Good Vibes**  
   - Craft a concise, reusable prompt.  
   - Ask for short answers and explicitly request “APIs current as of \<today’s date\>” to avoid stale code examples.

2. **Vibe but Verify**  
   - Don’t trust a single LLM. Ask two (e.g., ChatGPT & Claude) the same question and compare results—often one will catch what the other missed.

3. **Step Up the Vibe**  
   - Break your problem into small, independently testable chunks (e.g. function by function).  
   - If you’re not sure how to split it up, ask the LLM: “Outline 4–5 simple, testable steps for solving X.”

4. **Vibe & Validate**  
   - After one LLM writes the code, have a second LLM review or “lint” it:  
     > “Here’s my solution—please verify correctness, suggest improvements, and point out any bugs.”

5. **Vibe with Variety**  
   - Request multiple (e.g. three) different solutions to the same prompt.  
   - Compare approaches, pick the best, then ask that LLM to explain its rationale for deeper understanding.

> **Pro Tip:** Always finish by asking your LLM to explain the final code in plain terms. That way you’ll really know what’s happening under the hood when something eventually breaks!

---
Start vibing—just remember to stay in control.  

