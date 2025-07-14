# llm-tools-weather-forecast

[![PyPI](https://img.shields.io/pypi/v/llm-tools-weather-forecast.svg)](https://pypi.org/project/llm-tools-weather-forecast/)
[![Changelog](https://img.shields.io/github/v/release/thomd/llm-tools-weather-forecast?include_prereleases&label=changelog)](https://github.com/thomd/llm-tools-weather-forecast/releases)
[![Tests](https://github.com/thomd/llm-tools-weather-forecast/actions/workflows/test.yml/badge.svg)](https://github.com/thomd/llm-tools-weather-forecast/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/thomd/llm-tools-weather-forecast/blob/main/LICENSE)

Tool to get a current weather forecast for a given city

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-tools-weather-forecast
```
## Usage

To use this with the [LLM command-line tool](https://llm.datasette.io/en/stable/usage.html):

```bash
llm --tool weather_forecast "Example prompt goes here" --tools-debug
```

With the [LLM Python API](https://llm.datasette.io/en/stable/python-api.html):

```python
import llm
from llm_tools_weather_forecast import weather_forecast

model = llm.get_model("gpt-4.1-mini")

result = model.chain(
    "Example prompt goes here",
    tools=[weather_forecast]
).text()
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-tools-weather-forecast
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
