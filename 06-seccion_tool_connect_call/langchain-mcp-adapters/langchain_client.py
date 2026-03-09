import asyncio

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5:7b", temperature=0)

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "C:\\Users\\lftob\\Documents\\PROYECTOS_ESTUDIO\\ML_Engineer\\MCP_Udemy\\MCP_Crash_Course_Udemy\\06-seccion_tool_connect_call\\langchain-mcp-adapters\\servers\\math_server.py"
                ],
                "transport": "stdio"
            },
            "weather": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
        }
    )
    tools = await client.get_tools()
    agent = create_agent(llm, tools, debug=False)
    #result = await agent.ainvoke({"messages": "What is 2 + 2?"})
    result = await agent.ainvoke({"messages": "Cual es el clima en Medellín?"})

    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())