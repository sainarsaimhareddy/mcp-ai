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
    client = MCPClient.from_config_file(
        os.path.join(os.path.dirname(__file__),"browser_mcp.json")
    )
    print("currne  client ",client)
    # Create LLM
    # llm = ChatOpenAI(model="gpt-4o")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30,memory_enabled=True)
    user_input=str(input("Enter your query"))
    result = await agent.run( 
        user_input
    )
    print(f"Type: {type(result)}")
    print(f"Raw result: {result}")

# If it's a function or coroutine, try awaiting or calling it
    if callable(result):
        value = await result() if asyncio.iscoroutinefunction(result) else result()
        print("Final value:", value)

if __name__ == "__main__":
    asyncio.run(main())