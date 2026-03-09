import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(city: str) -> str:
    """Get weather for a city. Provide the city name as input. Uses open-meteo public API."""
    try:
        response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1")
        data = response.json()
        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
        data = response.json()
        weather = data["current_weather"]
        return f"The weather in {city} is {weather['temperature']}°C with {weather['windspeed']} km/h wind speed."
    except Exception as e:
        return f"Could not get weather for {city}: {e}"

if __name__ == "__main__":
    mcp.run(transport="sse")