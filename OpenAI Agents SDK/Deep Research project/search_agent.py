"""
   OpenAI Agents SDK includes the following hosted tools:
    
    - The `WebSearchTool` lets an agent search the web.  
    - The `FileSearchTool` allows retrieving information from your OpenAI Vector Stores.  
    - The `ComputerTool` allows automating computer use tasks like taking screenshots and clicking.
    
    - Structured output: the agent speaks JSON-ish so later stages can chain the data.  
    
    ### Important note - API charge of WebSearchTool
    
      `web_search` isn’t free:  
      - **≈ $0.025 per call** on `gpt-4o-mini` with *low* context.  
      - Deep research ≈ 10 searches ⇒ ~$0.25/run (watch our balance!).  
      - Dial *search_context_size* (`low | medium | high`) and/or switch models to save cents.
    
    * **Minimal agent skeleton**
    
      ```python
      search_agent = client.beta.assistants.create(
          name="Search Agent",
          instructions=(
              "You are a research assistant. Given a search term, "
              "search the web and produce a concise 2-3 paragraph summary. "
              "Succinct style; grammar not important."
          ),
          tools=[{"type": "web_search"}],                     # hosted tool
          model="gpt-4o-mini",                                # cheaper tier
          tool_resources={"web_search": {"search_context_size": "low"}},
          model_settings={"tool_choice": {"type": "required"}} # force the tool
      )


"""




import os
from agents import Agent, WebSearchTool, ModelSettings, function_tool
from Bio import Entrez


# For biotech focus (system prompt)
INSTRUCTIONS = (
    "You are a biotech research assistant for Genmab. Given a search term related to antibodies or cancer treatments, "
    "search the web and PubMed for that term and produce a concise summary of the results. Prioritize PubMed for scientific papers. "
    # Add guardrails:
    "Only use information directly from the search results; do not invent facts or add external knowledge. "
    "If data is missing (e.g., no results found), flag it explicitly in the summary with 'No relevant data found for [aspect]'. "
    "Think step-by-step: First, list key facts from sources; second, verify they align with the query; third, summarize without embellishment. "
    "The summary must be 2-3 paragraphs and less than 300 words. Capture main points like clinical trials, efficacy, and commercial implications. "
    "Write succinctly, no need for complete sentences or good grammar. This will be consumed by someone synthesizing a report, "
    "so capture the essence and ignore fluff. Do not include additional commentary."
)


@function_tool
def pubmed_search(query: str) -> str:
    """Search PubMed for biotech papers on the query."""
    Entrez.email = "vahedi.m1993@gmail.com"
    Entrez.api_key = os.getenv("NCBI_API_KEY")
    try:
        handle = Entrez.esearch(db="pubmed", term=query, retmax=5)
        record = Entrez.read(handle)
        ids = record["IdList"]
        if not ids:
            return "No results found on PubMed."
        fetch = Entrez.efetch(db="pubmed", id=ids, retmode="text")
        return fetch.read()
    except Exception as e:
        return f"PubMed error: {str(e)}. Falling back to web search only."


search_agent = Agent(
    name="Search Agent",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool(search_context_size="low"), pubmed_search],
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required")
)

