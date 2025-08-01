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




