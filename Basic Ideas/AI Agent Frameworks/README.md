## Agentic AI Framework Landscape

There are many frameworks with different trade-offs. Below is the simplified hierarchy:

### 1. No Framework / Direct API
- **What:** Call LLMs directly (e.g., OpenAI, Anthropic) without abstraction.
- **Pros:** Maximum visibility and control; simplest; easy to reason about prompts and behavior.
- **Used here:** Primary approach this week.  
- **Related protocol:** **MCP (Model Context Protocol)** – not a framework but an open, agreed-upon way to wire models to data/tools. It lives alongside “no framework” as a lightweight, composable convention.

### 2. Lightweight Frameworks
- **OpenAI Agents SDK**
  - Very light, flexible, minimal ceremony.
  - Keeps you close to the LLM while adding useful structure.
- **CrewAI**
  - Slightly higher-level; supports low-code composition (YAML/config).
  - Still lightweight but introduces some configuration abstractions.

### 3. Heavyweight Ecosystems
- **LangGraph** (from the LangChain authors) and **AutoGen** (Microsoft)
  - Much more powerful; build computational graphs of agents and tools.
  - Steeper learning curve and more ecosystem lock-in.

---

## Resources & Tools (Short Version)

### Resources
- **What:** “Resources” = extra context/data we give an LLM so it can answer better.  
  Example: for an airline support agent, include current ticket prices in the prompt so the model can refer to them.
- **Why:** Improves expertise and relevance by supplying facts up front instead of hoping the model “knows” them.
- **Smart retrieval:** Instead of dumping all data, we can *selectively fetch only the most relevant bits* (e.g., via similarity search or even with help from another LLM). This is the core idea behind **RAG** (Retrieval-Augmented Generation).
  - We retrieve context relevant to the user query.
  - We inject that into the prompt as the resource.

### Tools
- **What:** Granting an LLM the *ability to take actions* (e.g., query a database, call another service) by exposing "tools" it can invoke.
- **Mechanism (not magic):**
  1. Prompt the model with available actions/tools and instructions to respond in structured form (typically JSON).
  2. The model replies indicating what it wants to do, e.g.:  
     ```json
     { "action": "fetch_ticket_price", "args": { "destination": "Paris" } }
     ```
  3. Our code inspects that response (an `if`/dispatch), performs the requested action (e.g., fetch price), then calls the model again including the result.
- **Example flow:**
  - User: “How much is a flight to Paris?”
  - LLM (in JSON): `{ "action": "fetch_ticket_price", "args": { "city": "Paris" } }`
  - Code: Runs `fetch_ticket_price("Paris")`, gets price.
  - Code: Re-prompts LLM with original question + fetched price.
  - LLM: Generates final answer using the tool result.

- **Key point:** Tools give the LLM *discretionary autonomy* to decide “I need to run X” and then you execute it programmatically.

### Important Note on Tool Use

Tool calling isn’t magic—it’s just the LLM returning a structured JSON “intent” and our code acting on it (e.g., with simple `if`/dispatch logic). We prompt the model, it replies with what it wants to do in JSON, and our program executes that action and feeds back results. That's the whole pattern. 
---

## Evaluator-Optimizer Workflow (vanilla, no framework)

### Overview
1. Asking an LLM (e.g., GPT-4 or mini) a question.
2. Sending its answer to a separate **evaluator LLM** (e.g., Gemini) that returns a structured verdict (`is_acceptable: bool` + `feedback: str`) via a Pydantic schema (structured output).
3. If the answer fails evaluation, automatically **rerunning** the original LLM with context about the rejection to get an improved response.
4. Combining all of this into a single chat function: initial answer → evaluation → conditional retry.

### Workflow Summary
```python
# 1. Get answer from primary LLM (GPT-4/mini)
reply = ask_primary_llm(question)

# 2. Evaluate it via evaluator LLM (Gemini) with structured output
evaluation = evaluate(reply, question, history)  # returns object with is_acceptable & feedback

# 3. If rejected, rerun primary LLM with rejection context
if not evaluation.is_acceptable:
    reply = rerun_with_feedback(question, evaluation.feedback)

# 4. Return final answer




