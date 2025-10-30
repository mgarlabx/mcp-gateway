from fastmcp import Client
import asyncio

client = Client("https://mcp.peek.com")

async def main():
    async with client:
        result = await client.call_tool("search_experiences", {"query": "bike"})
        print(result)

if __name__ == "__main__":
    asyncio.run(main())