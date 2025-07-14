import llm


def weather_forecast(input: str) -> str:
    """
    Description of tool goes here.
    """
    return f"hello {input}"


@llm.hookimpl
def register_tools(register):
    register(weather_forecast)
