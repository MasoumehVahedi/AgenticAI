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


