import pandas as pd
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
import operator
from typing import Annotated, Any, Dict, List, Optional, Sequence, TypedDict

# The agent state is the input to each node in the graph
class AgentState(TypedDict):
    # The annotation tells the graph that new messages will always
    # be added to the current states
    messages: Annotated[Sequence[BaseMessage], operator.add]
    # The 'next' field indicates where to route to next
    next: str

def extract_csv_data(path_to_data: str) -> list:
    """
    Extracts data from a CSV file located at the specified `path_to_data` and prints the first row of the filtered data.

    Args:
        path_to_data (str): The path to the CSV file.

    Returns:
        pd.core.frame.DataFrame: The first row of the filtered data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        pd.errors.EmptyDataError: If the CSV file is empty.
        pd.errors.ParserError: If the CSV file cannot be parsed.

    """
    # Load the TYC dataset
    # The data is a pandas DataFrame object
    data = pd.read_csv(filepath_or_buffer=path_to_data)
    
    # Filter the data to get only the rows where the 'DONE' column is null
    # The filtered data is a pandas DataFrame object
    filtered_data = data.loc[data['DONE'] == 0]
    
    final_dict = {
        "filtered_data": filtered_data.iloc[0].to_dict(),
        "index_of_first_row": filtered_data.index[0]
    }
    
    # Return the first row of the filtered data and its index
    return final_dict

def create_agent(llm: ChatOpenAI, tools: list, system_prompt: str):
    """
    Creates an agent with the given language model, tools, and system prompt.

    Args:
        llm (ChatOpenAI): The language model used by the agent.
        tools (list): The list of tools to be used by the agent.
        system_prompt (str): The system prompt for the agent.

    Returns:
        AgentExecutor: The agent executor with the created agent and tools.
    """
    # Each worker node will be given a name and some tools.
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    agent = create_openai_tools_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools)
    return executor


def agent_node(state, agent, name):
    """
    Executes an agent node with the given state, agent, and name.

    Args:
        state (Any): The state to be passed to the agent.
        agent (Agent): The agent to be invoked.
        name (str): The name of the human message.

    Returns:
        dict: A dictionary containing a list of human messages.
    """
    result = agent.invoke(state)
    return {"messages": [HumanMessage(content=result["output"], name=name)]}
