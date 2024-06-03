# Direct Imports
import os
import utilities as ut
import tools

# From Packages Imports
from dotenv import load_dotenv
from llms import LLM

# Loading the environmental variables from the containing folder
load_dotenv(dotenv_path=r'.env')


# Add tracing in LangSmith
os.environ["LANGCHAIN_API_KEY"] = os.getenv(key="LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Multi-agent Collaboration"


# Extracting the csv data for the first row for an article which has NOT been generated
data_row = ut.extract_csv_data("data\TYC.csv")

# the title of the article to be generated
article_title = data_row["filtered_data"]["TITLE"]

# the URL of the article to be generated
article_url = data_row["filtered_data"]["URL"]

# the status of the article
article_done = data_row["filtered_data"]["DONE"]

# Agent creation
# members = ["Researcher", "Reviewer", "Revisor", "Writer", "Publisher", "SEO Extractor", "AI Graphic Designer"]
research_agent = ut.create_agent(
    llm=LLM.phi3,
    tools=[tools.search_tool],
    system_prompt="You are an expert web researcher."
)

reviewer_agent = ut.create_agent(
    llm=LLM.phi3,
    tools=[],
    system_prompt="You are web article reviewer with a keen eye for details"
)
revisor_agent = ut.create_agent(
    llm=LLM.phi3,
    tools=[],
    system_prompt="You are web article editor who can take detailed instructions and rewrite an article"
)
writer_agent = ut.create_agent(
    llm=LLM.phi3,
    tools=[],
    system_prompt="You are a expert web article writer"
)
publisher_agent = ut.create_agent(
    llm=LLM.phi3,
    tools=[],
    system_prompt="Given an article, image and keyword you can put together a final written piece for upload based on the website's specifications"
)
seo_extractor_agent = ut.create_agent(
    llm=LLM.phi3,
    tools=[],
    system_prompt="You can extract the keywords from any article"
)
ai_graphic_designer = ut.create_agent(
    llm=LLM.phi3,
    tools=[],
    system_prompt="Given a set of keywords you can generate a prompt which will be used to craft an image for an article"
)


# Node Creation