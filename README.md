# llm-tools-weather-forecast

Tool for the [llm CLI](https://github.com/simonw/llm) to get a current weather forecast for a given city.

> [!IMPORTANT]
> This tool was created for educational purposes only. It is not meant for production or the like.

## Installation

```bash
gh repo clone thomd/llm-tools-weather-forecast
cd llm-tools-weather-forecast
llm install --editable .
llm tools
```

## Usage

The tool requires an API Key from [OpenWeather](https://openweathermap.org/api).

```bash
export OPENWEATHERMAP_API_KEY="..."
llm --tool weather_forecast "What will the weather be like in Hamburg?" --tools-debug
```

## Analysis LLM Tool Calling

To understand how tools are processed by LLM models, use e.g. a local [Ollama](https://ollama.com/) model.

```bash
# start revers proxy
mitmproxy --mode reverse:http://localhost:11434@11435

# start Ollama server
OLLAMA_HOST=127.0.0.1:11434 ollama serve

# inspect llm requests in Mitmproxy
export OLLAMA_HOST=127.0.0.1:11435
llm --tool weather_forecast "What will the weather be like in Hamburg?" --no-stream
```
