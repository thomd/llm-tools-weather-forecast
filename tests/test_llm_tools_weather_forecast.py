import llm
import json
import pytest
from unittest.mock import patch, Mock
from llm_tools_weather_forecast import weather_forecast

@patch('llm_tools_weather_forecast.requests.get')
def test_tool(mock_get):

    def mock_requests(url):
        mock_response = Mock()
        if 'geo/1.0/direct' in url:
            mock_response.json.return_value = [{"lat": 0.0000, "lon": 0.0000}]
        elif 'data/2.5/forecast' in url:
            mock_response.json.return_value = {}
        return mock_response
    mock_get.side_effect = mock_requests

    model = llm.get_model("echo")
    chain_response = model.chain(
        json.dumps(
            {
                "tool_calls": [
                    {"name": "weather_forecast", "arguments": {"city_name": "Hamburg"}}
                ]
            }
        ),
        tools=[weather_forecast],
    )
    responses = list(chain_response.responses())

    tool_results = json.loads(responses[-1].text())["tool_results"]
    assert tool_results == [
        {"name": "weather_forecast", "output": "{}", "tool_call_id": None}
    ]
