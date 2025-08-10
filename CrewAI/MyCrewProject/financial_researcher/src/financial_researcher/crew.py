from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List


@CrewBase
class OpportunityRiskRadar:
    """Opportunity & Risk Radar crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ---- Agents ----
    @agent
    def signal_hunter(self) -> Agent:
        return Agent(config=self.agents_config["signal_hunter"], verbose=True, tools=[SerperDevTool()])

    @agent
    def finance_analyst(self) -> Agent:
        return Agent(config=self.agents_config["finance_analyst"], verbose=True)

    @agent
    def opportunity_architect(self) -> Agent:
        return Agent(config=self.agents_config["opportunity_architect"], verbose=True)

    @agent
    def guardrail_reviewer(self) -> Agent:
        return Agent(config=self.agents_config["guardrail_reviewer"], verbose=True)


    # ---- Tasks ----
    @task
    def signal_scan(self) -> Task:
        return Task(config=self.tasks_config["signal_scan"])

    @task
    def insight_build(self) -> Task:
        return Task(config=self.tasks_config["insight_build"])

    @task
    def action_plan(self) -> Task:
        return Task(config=self.tasks_config["action_plan"])

    @task
    def compliance_pass(self) -> Task:
        return Task(config=self.tasks_config["compliance_pass"])



    # ---- Crew ----
    @crew
    def crew(self) -> Crew:
        """Creates the Opportunity & Risk Radar crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
