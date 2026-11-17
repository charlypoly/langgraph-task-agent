"""Tools available to the agent."""

from datetime import datetime
from zoneinfo import ZoneInfo

from langchain_core.tools import tool


@tool
def get_current_time(time_zone: str = "UTC") -> str:
    """Return the current date and time in the given IANA time zone."""
    return datetime.now(ZoneInfo(time_zone)).isoformat()


@tool
def calculate(expression: str) -> str:
    """Evaluate a basic arithmetic expression like '(12 * 4) / 3'."""
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        return "Error: unsupported characters"
    return str(eval(expression, {"__builtins__": {}}, {}))


TOOLS = [get_current_time, calculate]
