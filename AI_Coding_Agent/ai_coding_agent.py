from crewai import Agent, Task, LLM, Crew, Process 
from crewai_tools import CodeInterpreterTool 
from crewai_tools import FileWriterTool 
from dotenv import load_dotenv 
import os

#Load all the environment variables
load_dotenv()

#Create Tools 
code_tool = CodeInterpreterTool()
write_tool = FileWriterTool()

#Define LLM 
llm = LLM(
    model = "gemini/gemini-2.5-flash",
    api_key = os.getenv("GOOGLE_API_KEY"),
    temperature= 0.7
)

#Define Agent and add tools to the agent 
agent = Agent(
    role = "Python Code Execution Specialist",
    goal = (
        "Take a natural‑language coding request, generate and run "
        "a Python script that solves it, capture its stdout, and "
        "persist any files as needed."
    ),
    backstory = (
         "You’re an expert Python developer and execution runtime. "
        "Your job is to translate user prompts into working scripts, "
        "run them reliably, and return both the code and its results."
    ),
    tools = [code_tool, write_tool],
    llm = llm,
    allow_code_execution = True,
    verbose  = True,
    allow_delegation = False
)

#Define Task 
task = Task(
    description= (
         "User has asked:\n\n"
        "{question}\n\n"
        "Generate the Python code to satisfy this request, execute it, "
        "and write out any output files via the File Writer tool."
    ),
    expected_output= "The actual code used to get the answer to the file.",
    agent = agent,
    llm = llm
)

#Define Crew 
crew = Crew(
    agents = [agent],
    tasks = [task],
    process = Process.sequential,
    verbose =True
)

#Kickoff 
question = input("Enter your code question: ")
result = crew.kickoff(inputs= {"question": question})

print(result)

