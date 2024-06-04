from dotenv import load_dotenv
from crewai_tools import SerperDevTool
load_dotenv()
import os
#os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY') 


api_key = os.getenv('SERPER_API_KEY')

if api_key is not None:
  os.environ['SERPER_API_KEY'] = api_key
else:
  print("Error: SERPER_API_KEY environment variable is not set.")


from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()