# backend.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ai_agent1 import get_response_from_ai_agent

# Allowed models (you can expand this list)
ALLOWED_MODELS = ["gpt-4o-mini", "llama3-70b-8192"]

# FastAPI app
app = FastAPI(title="LangGraph AI Agent API")

# Request schema
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with the AI agent.
    """
    # Validate model
    if request.model_name not in ALLOWED_MODELS:
        return {"error": "Requested AI model not supported."}

    try:
        # Get response from AI agent
        ai_reply = get_response_from_ai_agent(
            model_name=request.model_name,
            model_provider=request.model_provider,
            system_prompt=request.system_prompt,
            messages=request.messages,
            allow_search=request.allow_search,
            show_tool_calls=True  # set False to hide tool details
        )
        return {"reply": ai_reply}

    except Exception as e:
        return {"error": str(e)}


# Run locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
