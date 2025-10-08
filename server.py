from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import uvicorn

app = FastAPI(title="My Simple MCP Server")

# ----- Request model -----
class MCPRequest(BaseModel):
    method: str
    params: dict = {}

# ----- Endpoint -----
@app.post("/mcp")
def handle_mcp(req: MCPRequest):
    """Handles MCP requests for getting time and adding numbers."""
    if req.method == "get_time":
        return {"result": datetime.now().isoformat()}

    elif req.method == "add_numbers":
        a = req.params.get("a", 0)
        b = req.params.get("b", 0)
        return {"result": a + b}

    else:
        return {"error": f"Unknown method '{req.method}'"}

# ----- Run -----
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
