from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer
##forming the tech focused crew with some enhanced configurations

crew= Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    
)

# start the execution

result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)