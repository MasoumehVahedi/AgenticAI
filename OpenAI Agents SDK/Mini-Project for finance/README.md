

## Key Extensions to Our Agent Workflow

**1- Models Other Than OpenAI**

By default the SDK assumes we are using OpenAI’s endpoints.
If we pass in a string model name (e.g. "gpt-4o-mini"), it binds to OpenAI.

If we instead pass an **OpenAIChatCompletionsModel** instance with a custom base_url and key, we can drive any OpenAI-compatible LLM (Gemini, Groq, DeepSeek, local Llama, …).

**2- Structured Outputs**

Rather than free-form text, require our agent to return a JSON object with a fixed schema. Under the hood the SDK uses the LLM’s “function-call”/JSON API and deserializes straight into our Pydantic (or other) model.

**3- Guardrails**

Define checks on our agent’s inputs and outputs so we can catch bad or off-topic responses early. Think of guardrails as lightweight validators that wrap around our agent’s messages.
