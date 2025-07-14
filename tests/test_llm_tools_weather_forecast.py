import llm
import json
from llm_tools_weather_forecast import weather_forecast


def test_tool():
    model = llm.get_model("echo")
    chain_response = model.chain(
        json.dumps(
            {
                "tool_calls": [
                    {"name": "weather_forecast", "arguments": {"input": "pelican"}}
                ]
            }
        ),
        tools=[weather_forecast],
    )
    responses = list(chain_response.responses())
    tool_results = json.loads(responses[-1].text())["tool_results"]
    assert tool_results == [
        {"name": "weather_forecast", "output": "hello pelican", "tool_call_id": None}
    ]
