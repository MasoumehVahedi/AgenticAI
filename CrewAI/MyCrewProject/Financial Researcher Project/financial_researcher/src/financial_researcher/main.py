#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from financial_researcher.crew import OpportunityRiskRadar
from dotenv import load_dotenv
load_dotenv()  # loads variables from .env into environment

import os
print("OPENAI_API_KEY set:", bool(os.getenv("OPENAI_API_KEY")))

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the Opportunity Risk Radar crew.
    """

    inputs = {
        "company": "Visa",
        "industry": "payments",
        "peer_set": "Mastercard, American Express, Adyen",
        "theme": "real-time payments & network fees",
        "horizon": "90 days",
        "audience": "exec",  # exec | pm | sales
        "objective": "investment memo",
        "count": "12"  # for how many signals to return
    }

    result = OpportunityRiskRadar().crew().kickoff(inputs=inputs)
    print(f"Results: {result.raw}")


if __name__ == "__main__":
    run()
