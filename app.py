from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task = '''Go to google.com and go to linkedin login and then use email as ****** and 
            ***** as password and then enter AI Intern in the search textfield input at the top left and hit enter. This will show many job listings, then Search for Easy Apply option then
            Click on "Easy Apply" then
            Browse the filtered job listings, and look for the Easy Apply button next to the job title. Click on it to quickly apply without leaving LinkedIn.
            For Application purposes:
            If the fields are filled go ahead and click next  and if not try to check the label on the field and refer from the details below:
            Question : How many years of work experience do you have with GitHub? Answer : 8,
            Question : How many years of work experience do you have with Neuroscience? Answer : 0
            Question : How many years of work experience do you have with C++? Answer : 4,
            Question : How many years of work experience do you have with Python? Answer : 5,
            Question : Are you eligible to work in the country where the job is posted? Answer : Yes
            Question : Do you need sponsorship now or in future? Answer : Yes,
            Question : Can you start immediately? Answer : No
            
            If you dont have any answer to the question, write 3 for any experience related question or select No for any radio button selection question, and proceed to the next part of the application
            
            Keep on doing this until you have applied to all the jobs!''',
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
