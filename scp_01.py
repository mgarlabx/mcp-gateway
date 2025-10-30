from fastmcp import FastMCP

mcp = FastMCP("Teste")

@mcp.tool
def cotacao(ticker: str) -> float:
    """Retorna a cotação da ação (ticker) informada"""
    return 225

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)