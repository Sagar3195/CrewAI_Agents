from crewai import Crew 
from agents import researcher, writer 
from tasks import task1, task2
from crewai import Process

crew = Crew(
    agents = [researcher, writer],
    tasks = [task1, task2],
    verbose = True,
    process= Process.sequential

)

result = crew.kickoff()

print(result)

    