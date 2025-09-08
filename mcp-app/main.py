import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Use a supported model instead of the decommissioned one
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv()
    api_key=os.getenv('API_KEY')
    llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=api_key)
  

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_dict(
        os.path.join(os.path.dirname(__file__),"browser_mcp.json")
    )

    # Create LLM
    # llm = ChatOpenAI(model="gpt-4o")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "Find the best restaurant in San Francisco",
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())