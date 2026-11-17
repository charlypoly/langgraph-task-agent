from agent.tools import calculate


def test_calculate():
    assert calculate.invoke({"expression": "(2 + 3) * 4"}) == "20"
