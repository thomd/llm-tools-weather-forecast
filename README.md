# llm-tools-weather-forecast

Tool for the [llm CLI](https://github.com/simonw/llm) to get a current weather forecast for a given city.

[!IMPORTANT]
This tool was created for educational purposes only. It is not meant for production or the like.

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
llm --tool weather_forecast "What will the weather be like in Hamburg over the next three days?" --tools-debug
```

