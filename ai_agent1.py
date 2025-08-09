# ai_agent1.py

import os
from dotenv import load_dotenv
from typing import List

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, HumanMessage

# Load API keys from .env
load_dotenv()

# Tavily search tool (can be enabled/disabled per request)
search_tool = TavilySearch(max_results=2)

def get_response_from_ai_agent(
    model_name: str,
    model_provider: str,
    system_prompt: str,
    messages: List[str],
    allow_search: bool,
    show_tool_calls: bool = False
) -> str:
    """
    Creates an AI agent with given settings and returns the AI's reply.
    """
    # Select LLM
    if model_provider.lower() == "groq":
        llm = ChatGroq(model=model_name, temperature=0)
    elif model_provider.lower() == "openai":
        llm = ChatOpenAI(model=model_name, temperature=0)
    else:
        raise ValueError(f"Unsupported provider: {model_provider}")

    # Tools
    tools = [search_tool] if allow_search else []

    # Create the agent
    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # Prepare messages with optional system prompt
    chat_messages = []
    if system_prompt:
        chat_messages.append(SystemMessage(content=system_prompt))
    for msg in messages:
        chat_messages.append(HumanMessage(content=msg))

    # Invoke the agent
    result = agent.invoke({"messages": chat_messages})

    # Optionally show tool calls
    if show_tool_calls:
        for m in result["messages"]:
            if getattr(m, "type", None) == "tool":
                print("\n--- Tool Call ---")
                print(m)

    # Return only AI's final reply
    return result["messages"][-1].content

# Test run
if __name__ == "__main__":
    payload = {
        "model_name": "llama3-70b-8192",
        "model_provider": "Groq",
        "system_prompt": "You are a crypto expert AI.",
        "messages": ["Tell me about Bitcoin trends"],
        "allow_search": True
    }

    reply = get_response_from_ai_agent(
        model_name=payload["model_name"],
        model_provider=payload["model_provider"],
        system_prompt=payload["system_prompt"],
        messages=payload["messages"],
        allow_search=payload["allow_search"],
        show_tool_calls=True  # set False to hide
    )

    print("\n--- AI Reply ---")
    print(reply)
