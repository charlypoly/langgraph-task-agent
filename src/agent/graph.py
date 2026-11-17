"""A simple tool-calling agent graph."""

import os

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from agent.tools import TOOLS

load_dotenv()

SYSTEM_PROMPT = (
    "You are a helpful assistant that completes tasks for the user. "
    "Use the available tools when they help."
)

model = ChatOpenAI(model=os.getenv("MODEL", "gpt-6-astra")).bind_tools(TOOLS)


def call_model(state: MessagesState) -> dict:
    response = model.invoke([SystemMessage(SYSTEM_PROMPT), *state["messages"]])
    return {"messages": [response]}


builder = StateGraph(MessagesState)
builder.add_node("agent", call_model)
builder.add_node("tools", ToolNode(TOOLS))
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

graph = builder.compile(name="Task Agent")
