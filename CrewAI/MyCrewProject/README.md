## My Crew Project: Debate Setup

## Step-by-Step Process
1. **Open terminal in Cursor**

2. **Navigate to target directory**
   ```bash
   cd MyCrewProjec
   ```

3. Create a new Crew project

```bash
crew create crew PROJECT_NAME
```
- Choose OpenAI as model provider (or other ones)
- Select gpt-4 or gpt-4-mini (or any model we want)
- Press Enter at API key prompt (already in .env)

4. Understand scaffolding created
```bash
crew/
  PROJECT_NAME/
    knowledge/      # user preference (optional)
    src/PROJECT_NAME/     # main source directory
      config/       # configuration files
        agents.yaml
        tasks.yaml
      tools/        # placeholder tools
      crew.py       # crew setup
      main.py       # entry point
```
5. Key files

- agents.yaml: Defines agents
- tasks.yaml: Defines tasks

## Agent Configuration Overview (agents.yaml)

When defining agents in a Crew project, each agent should have:

1. **Role**  
   - A short description of what the agent represents or does.  
   - Example: "A compelling debater" or "Data analyst".

2. **Goal**  
   - The main objective or output the agent is expected to achieve.  
   - Can include template variables (e.g., `{topic}`, `{motion}`) for dynamic runtime values.

3. **Backstory**  
   - A descriptive context or persona for the agent.  
   - Serves as part of the system prompt to guide the LLM’s responses.

4. **Model**  
   - The AI model used by the agent.  
   - Defaults to **OpenAI**; can explicitly set models like `gpt-4` or `gpt-4-mini`.

### Template Variables
- Values in curly braces (e.g., `{motion}`) are placeholders.  
- They are set in your `main.py` at runtime and allow agents to work dynamically with different inputs.

### Backstory Importance
- The backstory is included in the prompt sent to the LLM.
- It influences the style, tone, and relevance of the agent’s responses.

### Best Practices
- Keep roles concise but specific.
- Make goals clear and measurable.
- Use template variables to keep agents reusable for different scenarios.
- Choose models balancing **quality** and **cost**.

