import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_ollama import ChatOllama
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

# Función para imprimir respuestas del LLM de forma bonita en consola
import re

def print_llm(response):
    """
    Imprime la respuesta del LLM en consola renderizando markdown si es posible.
    """
    try:
        from rich.console import Console
        from rich.markdown import Markdown
        console = Console()
        console.print(Markdown(str(response)))
    except ImportError:
        print(str(response))

# llm = ChatGoogleGenerativeAI()
llm = ChatOllama(model="qwen2.5:7b", temperature=0)

stdio_server_params = StdioServerParameters(
    command="python",
    args=["C:/Users/lftob/Documents/PROYECTOS_ESTUDIO/ML_Engineer/MCP_Udemy/MCP_Crash_Course_Udemy/06-seccion_tool_connect_call/langchain-mcp-adapters/servers/math_server.py"],
)

async def main():
    async with stdio_client(stdio_server_params) as (read,write):    
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialized")
            tools = await load_mcp_tools(session)
            agent = create_agent(llm, tools, debug=False)
            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 54 + 2 * 3?")]})
            print_llm(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())

