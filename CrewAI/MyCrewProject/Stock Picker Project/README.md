# CrewAI “Stock Picker” Project

This is the project in a nutshell: a clean, 4-agent Crew pipeline that finds, researches, and selects a stock, while demonstrating structured outputs, a custom tool, and hierarchical orchestration.

### What I have built:
A multi-agent CrewAI workflow that:
1. scans news to find trending companies in a sector,
2. researches each company,
3. picks the best one and explains why,
4. optionally notifies the user (custom tool).

### Pipeline
```bash
Manager (hierarchical) ──► TrendingCompanyFinder ──► FinancialResearcher ──► StockPicker
          plan/delegate            list of companies        research JSON         pick + report

```

### Why this works well

1. **Decomposition**: Each agent has a single responsibility.
2. **Determinism**: Structured outputs + consistent language reduce drift.
3. **Extensibility**: Swap models, add tools (web search, financial APIs), or add guardrails later.
4. **Observability**: Crew traces + explicit outputs (output/*.json, decision.md) make debugging easy.

### Extend
- Swap models per agent (Gemini/DeepSeek via OpenAI-compatible endpoints).
- Add more tools (Slack, email, CRM writeback).
- Add an **output guardrail** agent to check the final decision before notifying.


# Memory in CrewAI

CrewAI introduces a **memory system** that provides context to LLMs during execution.  
Instead of manually storing and passing variables, CrewAI gives built-in structures to manage memory.

---

## Goal of Memory
- Provide **contextual information** to LLMs at each call.
- Allow agents to **remember past interactions** and use them in future tasks.
- Reduce redundancy (e.g., not repeating the same recommendation).
- Enable more **personalized and context-aware AI behavior**.

---

## Advantages
- **Faster setup**: Predefined memory types make it easy to use.
- **Context retention**: Agents have awareness of prior steps, improving decisions.
- **Structured knowledge**: Combines vector search and SQL for richer recall.
- **Flexibility**: We can choose which agents should "remember" or stay stateless.
- **Scalability**: Supports multiple memory types for complex multi-agent workflows.

---

## Trade-offs
- **Less transparency**: Harder to debug prompts since memory is abstracted.
- **Learning curve**: Requires understanding how CrewAI manages memory behind the scenes.
- **Manual setup for some cases**: e.g., user memory still needs explicit handling.

---

## Types of Memory

1. **Short-Term Memory**  
   - Stores **recent interactions** and outcomes.  
   - Uses **RAG (vector database)** for quick retrieval during execution.

2. **Long-Term Memory**  
   - Stores **important knowledge** over time.  
   - Uses **SQLite** for persistence and recall.  
   - Builds cumulative insights for the project.

3. **Entity Memory**  
   - Stores information about **people, places, and concepts**.  
   - Enables deeper understanding and relationship mapping.  
   - Uses **RAG similarity search**.

4. **Contextual Memory**  
   - An **umbrella** that combines short-term, long-term, and entity memory.  
   - Provides unified context to LLMs with minimal configuration.

5. **User Memory**  
   - Stores **user-specific information and preferences**.  
   - Enhances personalization and user experience.  
   - Currently requires manual management.

---

##  Key Insight
At the end, **memory = more relevant context added to prompts**.  
By enabling memory, LLMs gain awareness of prior interactions, making them:  
- Smarter  
- Less repetitive  
- More aligned with user needs  

---

##  Example Use Case: Stock Picker Project
- **Short-Term Memory**: Tracks recent queries and avoids duplicate recommendations.  
- **Long-Term Memory**: Saves past results in SQL for knowledge building.  
- **Entity Memory**: Stores company-related entities for better recommendations.  
- **Result**: The AI can recommend *new companies* without repeating the same stock.  

---

✨ Memory transforms CrewAI agents into **context-aware, evolving systems**, giving them persistence across interactions.


