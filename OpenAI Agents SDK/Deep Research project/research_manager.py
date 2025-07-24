from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from agents import Runner, trace, gen_trace_id
from search_agent import search_agent
from clarifier_agent import clarifier_agent
from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from writer_agent import writer_agent, ReportData
from email_agent import email_agent
import asyncio




class ResearchManager:

    async def run(self, query: str):
        """ Run the deep research process, yielding the status updates and the final report"""
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
            yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            print("Starting research...")
            search_plan = await self.plan_searches(query)
            yield "Searches planned, starting to search..."
            search_results = await self.perform_searches(search_plan)
            yield "Searches complete, optimizing results..."
            optimized_results = self.optimize_results(search_results, query)
            yield "Optimization complete, writing report..."
            report = await self.write_report(query, optimized_results)
            yield "Report written, sending email..."
            await self.send_email(report)
            yield "Email sent, research complete"
            yield report.markdown_report

    async def plan_searches(self, query: str) -> WebSearchPlan:
        """ Plan the searches to perform for the query """
        print("Planning searches...")
        result = await Runner.run(
            planner_agent,
            f"Query: {query}",
        )
        print(f"Will perform {len(result.final_output.searches)} searches")
        return result.final_output_as(WebSearchPlan)


    async def perform_searches(self, search_plan: WebSearchPlan) -> list[str]:
        """ Perform the searches to perform for the query """
        print("Searching...")
        num_completed = 0
        tasks = [asyncio.create_task(self.search(item)) for item in search_plan.searches]
        results = []
        for task in asyncio.as_completed(tasks):
            result = await task
            if result is not None:
                results.append(result)
            num_completed += 1
            print(f"Searching... {num_completed}/{len(tasks)} completed")
        print("Finished searching")
        return results


    def optimize_results(self, results: list[str], query: str) -> list[str]:
        """Optimize search results by ranking relevance (TF-IDF)."""
        if not results:
            return []
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([query] + results)
        similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
        sorted_indices = similarities.argsort()[::-1]
        filtered = [results[i] for i in sorted_indices if similarities[i] > 0.01]
        print(f"Optimized from {len(results)} to {len(filtered)} results.")
        return filtered


    async def search(self, item: WebSearchItem) -> str | None:
        """ Perform a search for the query """
        input = f"Search term: {item.query}\nReason for searching: {item.reason}"
        try:
            result = await Runner.run(
                search_agent,
                input,
            )
            return str(result.final_output)
        except Exception:
            return None

    async def write_report(self, query: str, search_results: list[str]) -> ReportData:
        """ Write the report for the query """
        print("Thinking about report...")
        input = f"Original query: {query}\nSummarized search results: {search_results}"
        result = await Runner.run(
            writer_agent,
            input,
        )
        print("Finished writing report")
        return result.final_output_as(ReportData)


    async def send_email(self, report: ReportData) -> None:
        print("Writing email...")
        try:
            result = await Runner.run(
                email_agent,
                report.markdown_report,
            )
            # Debug
            #print(f"Email result: {result}")
            print("Email sent")
        except Exception as e:
            print(f"Email failed: {str(e)}")
        return report

