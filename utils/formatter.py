def format_weather(data):
    name = data["name"]
    temp = data["main"]["temp"]
    weather_desc = data["weather"][0]["description"].title()
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    return (
        f"Weather in {name}:\n"
        f"🌡 Temperature: {temp}°C\n"
        f"🌥 Condition: {weather_desc}\n"
        f"💧 Humidity: {humidity}%\n"
        f"💨 Wind Speed: {wind} m/s"
    )
