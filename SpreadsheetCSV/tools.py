from crewai_tools import CSVSearchTool 
import os
from dotenv import load_dotenv 
load_dotenv()

#It requires openapie key not other keys
tool = CSVSearchTool(csv = "IT_salaries.csv",
                    api_key = os.getenv("GOOGLE_API_KEY")
                    )

