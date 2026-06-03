from datetime import datetime
from zoneinfo import ZoneInfo

from geopy.geocoders import Nominatim
from google.adk.agents.llm_agent import Agent
from timezonefinder import TimezoneFinder


# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time for ANY city using geocoding."""
    geolocator = Nominatim(user_agent="agent_time_tool")
    tf = TimezoneFinder()

    try:
        location = geolocator.geocode(city)
        if location:
            tz_string = tf.timezone_at(lng=location.longitude, lat=location.latitude)
            real_time = datetime.now(ZoneInfo(tz_string)).strftime("%I:%M %p")
            return {"status": "success", "city": city, "time": real_time}
        else:
            return {
                "status": "error",
                "message": f"Could not locate the city '{city}'.",
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}


root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)
