## 🚢 CrewAI Overview

* **Three commercial offerings**  
  | Product | What it is | 
  |---------|------------|
  | **CrewAI Enterprise** | Hosted platform for deploying / running / monitoring agents | 
  | **CrewAI UI Studio**  | Low-/no-code drag-n-drop builder | 
  | **CrewAI open-source framework** | Python framework to “orchestrate high-performing AI agents with ease & scale” | 

  *Note — unlike OpenAI/Anthropic (who monetize via models), CrewAI must upsell Enterprise & Studio for revenue, so the docs/website push those heavily.*

* **Two “flavors” in the framework**  
  | Flavor | Use when… | Characteristics |
  |--------|-----------|-----------------|
  | **Crews** | Need **autonomous** problem-solving, creative collaboration, exploratory tasks | Teams of agents with distinct roles |
  | **Flows** | Need **deterministic** outcomes, strict auditability, precise control | Prescribed, step-by-step workflows |

  I will focus on **Crews**, because it is about fully agentic autonomy.


---

## CrewAI Core Concepts & Scaffold

### 1. Key building blocks
| Element | What it is | Notes |
|---------|------------|-------|
| **Agent** | Autonomous unit backed by an LLM | needs **role · goal · back-story** (+ optional memory & tools) |
| **Task**  | Single assignment tied to *one* agent | has **description · expected output** |
| **Crew**  | Collection of Agents + Tasks | runs in **Sequential** (tasks in order) *or* **Hierarchical** (manager-LLM delegates) mode |

> Compared to OpenAI Agents SDK, CrewAI is **more opinionated**—it forces us to think in terms of role/goal/back-story instead of a single free-form “instructions” string.

---

### 2. YAML-first configuration
```yaml
researcher:
  role:  Senior Financial Researcher
  goal:  Research companies, news & potential backstory
  backstory: |
    We are a seasoned financial researcher with a talent for finding the most relevant information.
  llm: openai/gpt-4o-mini
```

**Pros**: clean separation of prompts from code, easy to tweak
**Cons**: extra scaffold specific to CrewAI

We can then instantiate with:
```python
agent = Agent(config=self.agents_config['researcher'])
```

### 3. crew.py — where it all comes together
```python
from crew import CrewBase, agent, task, crew, Process

@CrewBase
class MyCrew:
    @agent
    def researcher(self) -> Agent:        # ← pulled from YAML
        ...

    @task
    def market_scan(self) -> Task:        # ← also YAML-backed
        ...

    @crew
    def assemble(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.SEQUENTIAL   # or HIERARCHICAL
        )

```

Decorators automatically register each function to self.agents / self.tasks, keeping boilerplate minimal.


### 4. Mental model / trade-offs

- **Opinionated prompts** = helpful defaults but less low-level control of the final system prompt.
- **YAML + decorators** give neat separation of concerns, at the cost of extra files to grok.
- Choose **Crews** for autonomous, exploratory work; **Flows** when you need deterministic, auditable pipelines.







