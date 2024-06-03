from typing import TypedDict


class DraftState(TypedDict):
    """
    This TypedDict class contains the state of a draft agent.

    Attributes:
        task (dict): A dictionary representing the task that the agent is working on.
        topic (str): The topic of the draft.
        draft (dict): A dictionary containing the draft of the article.
        review (str): The review of the draft by the reviewer.
        revision_notes (str): The notes of the revised draft.
    """
    task: dict
    topic: str
    draft: dict
    review: str
    revision_notes: str
