from langchain.tools import StructuredTool, tool
from gpt_researcher import GPTResearcher
from dotenv import load_dotenv
import os

# Loading environment variables
load_dotenv('.env')

os.environ["LLM_PROVIDER"] = os.getenv("LLM_PROVIDER")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["FAST_LLM_MODEL"] = os.getenv("FAST_LLM_MODEL")
os.environ["SMART_LLM_MODEL"] = os.getenv("SMART_LLM_MODEL")


async def search_tool(query: str, report_type: str, sources: list) -> str:
    researcher = GPTResearcher(query=query, report_type=report_type, source_urls=sources)
    await researcher.conduct_research()
    report = await researcher.write_report()
    return report

search = StructuredTool.from_function(
    func=search_tool,
    name="Search",
    description="Produces detailed, factual and unbiased research reports, with customization options for focusing on relevant resources, outlines, and lessons and useful for when you need to answer questions about current events",
)

