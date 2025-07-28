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

