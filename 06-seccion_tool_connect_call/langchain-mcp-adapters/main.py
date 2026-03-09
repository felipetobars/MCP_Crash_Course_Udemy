import asyncio
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
print(os.getenv("GOOGLE_API_KEY"))

async def main():
    print("Hello from langchain-mcp-adapters!")


if __name__ == "__main__":
    asyncio.run(main())
