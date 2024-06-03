from typing import TypedDict, List


class ResearchState(TypedDict):
    """
    A TypedDict that represents the state of the research agent.

    Attributes:
        task (dict): A dictionary representing the task that the agent is working on.
        initial_research (str): The initial research that the agent starts with.
        sections (List[str]): A list of sections that the agent will research.
        research_data (List[dict]): A list of dictionaries containing the research data.
        title (str): The title of the report generated by the agent.
        headers (dict): The headers of the report generated by the agent.
        date (str): The date of the report generated by the agent.
        table_of_contents (str): The table of contents of the report generated by the agent.
        introduction (str): The introduction of the report generated by the agent.
        conclusion (str): The conclusion of the report generated by the agent.
        sources (List[str]): The sources of the report generated by the agent.
        report (str): The final report generated by the agent.
    """
    task: dict
    initial_research: str
    sections: List[str]
    research_data: List[dict]
    # Report layout
    title: str
    headers: dict
    date: str
    table_of_contents: str
    introduction: str
    conclusion: str
    sources: List[str]
    report: str

