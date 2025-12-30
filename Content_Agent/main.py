from crewai import Crew, Task, LLM, Agent 
from crewai_tools import BrowserbaseLoadTool, EXASearchTool, SerperDevTool 
from dotenv import load_dotenv
import os 

#Load all the environment variables
load_dotenv()

# Define LLM model
llm = LLM(
    model = "gemini/gemini-2.5-flash",
    api_key = os.getenv("GOOGLE_API_KEY"),
    temperature= 0.7
)

# Define Tools
# browser_tool = BrowserbaseLoadTool()
browser_tool = SerperDevTool()
# exa_tool = EXASearchTool()

# Define Agents
researcher_agent = Agent(
    role = "Content Researcher",
    goal = "Research information on a given topic and prepare structured notes.",
    backstory = "You gather credible information from trusted sources and summarize it in a clear format.",
    tools = [browser_tool],
    llm = llm,
    verbose = True   
)

writer_agent = Agent(
    role = "Senior Content Writer",
    goal = "Write a polished article based on the research notes.",
    backstory = "You create clean and engaging content from research findings.",
    llm = llm,
    verbose = True
)

# Create the Task
from crewai import Task

research_task = Task(
    description="Research the topic and produce a structured set of notes with clear headings.",
    expected_output="A well-organized research summary about the topic.",
    agent=researcher_agent,
)

write_task = Task(
    description="Write a clear final article using the research notes from the first task.",
    expected_output="A polished article that covers the topic thoroughly.",
    agent=writer_agent,
)

# Define the Crew
crew = Crew(
    agents = [researcher_agent, writer_agent],
    tasks = [research_task, write_task],
    planning= True,
    
)

# Run the crew
result = crew.kickoff(inputs={"topic":"AI Agent Roadmap", "todays_date": "Dec 1, 2025"})

print(result)

