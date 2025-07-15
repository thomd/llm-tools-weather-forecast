# llm-tools-weather-forecast

Tool for the [llm CLI](https://github.com/simonw/llm) to get a current weather forecast for a given city.

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

The tool requires an API Key from [OpenWeather](https://openweathermap.org/api).

```bash
export OPENWEATHERMAP_API_KEY="..."
llm --tool weather_forecast "What will the weather be like in Hamburg?" --tools-debug
```

