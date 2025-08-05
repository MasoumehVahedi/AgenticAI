"""
    Writer Agent 

    **Writer (“Researcher”) Agent**  
      - Prompt: “You are a *senior researcher*; given the query *and* the assistant’s raw search notes, draft a full report.”  
      - Output spec: `ReportData` (Pydantic)  
        ```python
        class ReportData(BaseModel):
            short_summary:     str      # 2–3-sentence Too Long; Didn’t Read.
            markdown_report:   str      # 5–10 pages, ≥1000 words
            follow_up_questions: list[str]  # suggested next-step research
        ```
      - Model: `gpt-4o-mini` (cheap); `output_type=ReportData` forces JSON-backed structured output.
    
"""


from pydantic import BaseModel
from agents import Agent


INSTRUCTIONS = (
    "You are a senior biotech researcher for Genmab tasked with writing a cohesive report for a research query. "
    "You will be provided with the original query, and some initial research done by a research assistant.\n"
    "You should first come up with an outline for the report that describes the structure and "
    "flow of the report. Then, generate the report and return that as your final output.\n"
    "Only use information from the provided search results; do not invent facts or assume unprovided details. "
    "If data is missing for key aspects (e.g., no clinical trial info), flag it in the report with 'Data gap: No information available on [aspect]; further research recommended'. "
    "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
    "for 5-10 pages of content, at least 1000 words."
)


class ReportData(BaseModel):
    short_summary: str
    """A short 2-3 sentence summary of the findings."""

    markdown_report: str
    """The final report"""

    follow_up_questions: list[str]
    """Suggested topics to research further"""



writer_agent = Agent(
    name="WriterAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=ReportData,
)




