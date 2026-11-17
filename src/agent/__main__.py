"""Run the agent from the command line: python -m agent "your task"."""

import sys

from agent.graph import graph


def main() -> None:
    task = " ".join(sys.argv[1:]) or "What time is it in Tokyo?"
    result = graph.invoke({"messages": [("user", task)]})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
