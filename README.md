# llm-tools-weather-forecast

[![Tests](https://github.com/thomd/llm-tools-weather-forecast/actions/workflows/test.yml/badge.svg)](https://github.com/thomd/llm-tools-weather-forecast/actions/workflows/test.yml)

Very simple tool for the [llm](https://github.com/simonw/llm) CLI to get a current weather forecast for a given city.

> [!CAUTION]
> This tool was created for educational purposes only. It is not meant for production or the like.

## Installation

```bash
gh repo clone thomd/llm-tools-weather-forecast
cd llm-tools-weather-forecast
llm install --editable .
llm tools
```

## Usage

The tool requires an API Key from [OpenWeatherMap](https://openweathermap.org/api).

```bash
export OPENWEATHERMAP_API_KEY="..."
llm --tool weather_forecast "What will the weather be like in Hamburg?" --tools-debug
llm --tool weather_forecast -s "Act as a meteorologist" "What will the weather be like in Hamburg tomorrow?"
```

## Analysis LLM Tool Calling

To understand how python code of tools is translated to the API structure of requests, use a local [Ollama](https://ollama.com/) 
model and start [mitmproxy](https://mitmproxy.org/) as a reverse proxy for inspection of the request and response.

```bash
# start revers proxy
mitmproxy --mode reverse:http://localhost:11434@11435

# start Ollama server
OLLAMA_HOST=127.0.0.1:11434 ollama serve

# inspect llm requests in Mitmproxy
export OLLAMA_HOST=127.0.0.1:11435
llm --tool weather_forecast "What will the weather be like in Hamburg?" --no-stream
```
