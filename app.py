from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Go to google.com and go to linkedin login and then use email as ananyd36@gmail.com and apdjpr@22 as password and then go to linkedin search and search for jobs as an ai intern",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())