from crewai import Task 
from agents import researcher, writer 


task1 = Task(
    description="""Using the csv file named 'IT_salaries.csv extract the top 10 rows with the highest salaries in the entire csv file based on the column 'Yearly brutto salary (without bonus and stocks) in EUR
                ' and rank them based on the column 'Position' and column 'Your main technology / programming language'. DO NOT deviate from the actual content of the csv file; then present them in a structured format.""",
    expected_output="top 10 rows based on salaries in a structured format",
    agent=researcher
)

task2 = Task(
    description="""Using the structured data and insights provided by the Expert Data Analyst agent, develop a precise technical report that highlights the most important skills, technologies, and programming languages needed to obtain highest salaries in the IT sector, then from your knowledge explain a brief overview of the path and timeline required to obtain that skills, technology, or programming language.""",
    expected_output="Technical report and explanation of at least 1000 words",
    agent=writer,
    output_file='IT_salaries.md'  # Example of output customization
)





