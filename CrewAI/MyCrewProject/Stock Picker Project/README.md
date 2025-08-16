# CrewAI “Stock Picker” Project

This is the project in a nutshell: a clean, 4-agent Crew pipeline that finds, researches, and selects a stock, while demonstrating structured outputs, a custom tool, and hierarchical orchestration.

### What I have built:
A multi-agent CrewAI workflow that:
1. scans news to find trending companies in a sector,
2. researches each company,
3. picks the best one and explains why,
4. optionally notifies the user (custom tool).

### Pipeline
```bash
Manager (hierarchical) ──► TrendingCompanyFinder ──► FinancialResearcher ──► StockPicker
          plan/delegate            list of companies        research JSON         pick + report

```

### Why this works well

1. **Decomposition**: Each agent has a single responsibility.
2. **Determinism**: Structured outputs + consistent language reduce drift.
3. **Extensibility**: Swap models, add tools (web search, financial APIs), or add guardrails later.
4. **Observability**: Crew traces + explicit outputs (output/*.json, decision.md) make debugging easy.
