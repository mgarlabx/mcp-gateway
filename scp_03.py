from fastmcp import FastMCP, Client

mcp = FastMCP("Teste")

@mcp.tool
async def search_experiences(query: str) -> float:
    """Search for travel experiences with comprehensive filtering options. Returns available categories, tags, and regions with IDs for further filtering."""
    client = Client("https://mcp.peek.com")
    async with client:
        result = await client.call_tool("search_experiences", {"query": "bike"})
        return result

@mcp.tool
async def ListRemoteMCPServers(query: str) -> float:
    """List all available remote MCP servers for a specific query."""
    client = Client("https://mcp.remote-mcp.com")
    async with client:
        result = await client.call_tool("ListRemoteMCPServers", {"query": query})
        return result

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)