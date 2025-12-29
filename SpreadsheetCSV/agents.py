from crewai import Agent
from crewai import LLM 
from dotenv import load_dotenv 
import os 
from tools import tool

#Loadint the environment variable
load_dotenv()

#Define LLM model 
llm = LLM(model = "gemini/gemini-2.0-flash",
          api_key = os.getenv("GOOGLE_API_KEY"),
          temperature= 0.7
        )


#Agent 1: Researcher 
researcher = Agent(
        role = "Expert Data Analyst",
        goal = "Extract the relevant data from CSV file and structure them as instructed.",
        backstory = """You are an expert data analyst for extracting information from CSV files as instructed in the task description.""",
        allow_delegation = False,
        verbose = True,
        llm = llm,
        tool = [tool]

)

#Agent 2: Writer 
writer = Agent(
        role = "Techincal Report Writer",
        goal = """Summarise the researcher's responses in relevant and precise steps and then write technical report on the summarised data using your knowledge""",
        backstory = """You are an expert in writing AI-related technical report for individual tech enthusiasts; produce a detailed report in simple language""",
        allow_delegation = False,
        verbose = True,
        llm = llm

)


