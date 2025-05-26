from flask import Flask, render_template_string, request
from weather.fetcher import get_weather
from weather.location import get_location_city
from utils.formatter import format_weather

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>Weather App</title>
<h2>🌦 Weather App</h2>
<form method="post">
    <input name="city" placeholder="Enter city (or leave blank to auto-detect)" size="40">
    <button type="submit">Get Weather</button>
</form>
{% if result %}
<pre>{{ result }}</pre>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    city = ""
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if not city:
            city = get_location_city()
        try:
            weather = get_weather(city)
            result = format_weather(weather)
        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
