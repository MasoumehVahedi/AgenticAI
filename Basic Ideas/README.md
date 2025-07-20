## 🤖 What Is an Agent? (Agentic AI Explained)

"AI agents are programs where LLM outputs control the workflow."

This simple definition from Hugging Face captures the core idea: when the **output of an LLM** (large language model) can **decide the next steps**, we call it **Agentic AI**.

### ✨ Hallmarks of Agentic AI

A system is often called "agentic" if it includes any of the following:

1. **Multiple LLM calls**  
   - Each output feeds into the next step, simulating reasoning over time.

2. **LLMs using tools**  
   - For example, a model that calls APIs, searches the web, or runs code.

3. **LLMs coordinating with other LLMs**  
   - A multi-agent setup where LLMs communicate and delegate tasks.

4. **A planner component**  
   - A system that plans task sequences based on the goal and LLM outputs.

5. **Autonomy**  
   - The LLM is free to choose which action to take next.

---

### 🧠 Autonomy vs. Workflows

According to Anthropic’s framework in *"Building Effective Agents"*, there are two subtypes of agentic systems:

- **Workflows**:  
  LLMs and tools are orchestrated through predefined code paths.

- **Agents**:  
  LLMs dynamically decide what tools to use and in what order — maintaining **control** over the process.

While some solutions people call “agents” are actually structured workflows, both fall under the broader concept of **agentic AI**.

---

### 💡 Summary

Agentic AI systems allow LLMs to do more than answer a prompt — they let the model **drive decisions, plan, act, and adapt**.

Whether using one model step-by-step or coordinating many, these systems mimic reasoning and autonomy — making AI not just smart, but also **interactive and goal-directed**.

---


## Category 1: Workflow Design Patterns
These are structured, fixed-path designs. Tasks are broken into known steps—deterministic and repeatable.

Anthropic defines **five** foundational patterns to structure AI workflows involving LLMs. These help decompose, route, validate, and parallelize complex tasks across multiple LLMs.

---

## 1. Prompt Chaining

### Concept:
Decompose a task into **a fixed set of subtasks**, each handled by an LLM. You can optionally insert code between steps.

```text
INPUT → LLM1 → [Code/Gate] → LLM2 → LLM3 → OUTPUT
```

### Example:
You want to generate a business idea.
- LLM1: Picks a business domain (e.g., education)
- [Code/Gate]: Cleans or transforms the output (optional)
- LLM2: Identifies a pain point in that domain (e.g., lack of access in rural areas)
- LLM3: Proposes a solution (e.g., AI-powered tutoring app)
- OUT: Final result = a detailed business proposal

### Benefits:
- Modular design — easy to debug each step
- Precision in prompting each LLM
- Encourages explainability and traceability
- Optional code inserts for rule-based decisions

---

## 2. Routing

### Concept:
An LLM acts as a **router**, directing input to the most suitable expert LLM based on task classification.

```text
INPUT → LLM Router → LLM1 / LLM2 / LLM3 → OUTPUT
```
### Example:
You get a customer service question.
- LLM Router: Classifies it as either “billing”, “tech support”, or “product”
- If “billing”: → LLM1 handles it
- If “tech”: → LLM2 handles it
- If “product”: → LLM3 handles it

### Benefits:
- Uses expert models trained for narrow domains
- Clear separation of concerns
- Efficient model utilization
- Dynamic but controlled decision-making

---

## 3. Parallelization
### Concept:
Code (not an LLM) splits a task into multiple subtasks to be run in parallel by different LLMs. The outputs are later merged.

```text
INPUT → [Coordinator Code] → LLM1 / LLM2 / LLM3 (in parallel) → [Aggregator Code] → OUTPUT
```

### Example:
You want to summarize a long research paper.
- Coordinator code splits it into sections (intro, methods, results)
- Each LLM summarizes one section simultaneously
- Aggregator code joins them into a cohesive summary

### Benefits:
- Improves speed via concurrent execution
- Efficient for large-scale or batch processing
- Aggregation allows customized stitching logic
- Task distribution is deterministic and transparent

---

## 4. Orchestrator-Worker

### Concept:
An LLM orchestrator dynamically breaks down complex tasks, assigns pieces to worker LLMs, and a synthesizer recombines results.

```text
INPUT → LLM Orchestrator → Worker LLMs → LLM Synthesizer → OUTPUT
```
### Example:
You want to generate a market report.
- Orchestrator LLM decides on subtasks: “research trends”, “analyze competitors”, “predict demand”
- Each task goes to a specialized Worker LLM
- Synthesizer LLM combines their results into a unified report

### Benefits:
- No fixed subtask list — it's dynamic
- LLM orchestrator brings autonomy
- Useful for complex, evolving tasks
- Feels more "agent-like" while still structured

---

## 5. Evaluator-Optimizer
One LLM generates an answer, another evaluates it. If rejected, feedback is sent and a retry is triggered — creating a validation loop.

```text
INPUT → LLM Generator → LLM Evaluator 
              ↳ [Reject + Feedback] → Generator (retry)
              ↳ [Accept] → OUTPUT
```

### Example:
You're building a math tutor.
- LLM Generator: Solves a math problem
- LLM Evaluator: Verifies if the solution is correct
- If wrong: gives error message and asks for retry
- If right: passes answer to user

### Benefits:
- Boosts correctness and reliability
- Validation loop reduces hallucinations
- Ideal for safety-critical use cases
- Encourages high-quality output via feedback cycles

---

## Category 2: Agentic Patterns
By contrast, Agentic Patterns are open-ended.
LLMs interact with environments, receive feedback, and choose their own paths.

### Key traits:
- ✅ Open-ended & flexible
- 🔁 Feedback loops
- 🚫 No fixed sequence of actions
- 🤖 LLM autonomously controls the flow

### Example structure:

```text
[Human] → LLM ↔ Environment (Action ↔ Feedback)
         ↓
        STOP (when agent chooses)
```

### ⚠️ Risks of Agentic Frameworks
While powerful, agentic systems introduce uncertainty and cost overheads that require careful mitigation.

Common Challenges:
- Unpredictable Path: LLM decides the action order dynamically.
- Unpredictable Output: No guaranteed accuracy or success.
- Unpredictable Costs: Repeated LLM/tool usage may increase API bills.

 ### Risk Mitigation Strategies
#### 1. Monitor Everything
Track LLM behavior, calls, and feedback loops. Especially important with multi-agent environments.

```text
Trace interactions → Understand inner workings → Detect issues early
```

OpenAI SDK & LangSmith provide tools for tracing and visibility.

#### 2. Guardrails
Write constraints in code to define safety, ethical limits, and behavioral boundaries.

Guardrails ensure your agents:
- Behave safely
- Stay within scope
- Don’t take harmful or unproductive actions

These protections are essential when deploying agentic AI in production systems.


---

## The Cast of LLM Characters

These are the key LLM providers we will encounter during agentic AI development:

- **OpenAI**: gpt-4o-mini (also gpt-4o, o1, o3-mini)
- **Anthropic**: Claude-3-7-Sonnet
- **Google**: Gemini-2.0-Flash
- **DeepSeek AI**: DeepSeek V3, DeepSeek R1
- **Groq**: Open-source LLMs incl. Llama3.3
- **Ollama**: Local open-source LLMs incl. Llama3.2

For comparison of cost, speed, and performance, check:
[https://www.vellum.ai/llm-leaderboard](Vellum Leaderboard)









