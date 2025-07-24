from pydantic import BaseModel, Field
from agents import Agent

HOW_MANY_SEARCHES = 15

INSTRUCTIONS = f"You are a biotech research assistant for Genmab. Given a query on topics like bispecific antibodies or cancer treatments, "
f"come up with a set of web and PubMed searches to best answer it. Focus on Genmab's KYSO medicines, clinical trials, and commercial impacts. "
f"Output {HOW_MANY_SEARCHES} terms to query for, including scientific angles."


class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query, e.g., for Genmab's R&D insights.")
    query: str = Field(description="The search term to use for the web or PubMed search.")


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of searches to perform, tailored for biotech relevance.")


planner_agent = Agent(
    name="PlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan,
)


