from weather.fetcher import get_weather
from utils.formatter import format_weather

def main():
    city = input("Enter city name: ")
    try:
        weather_data = get_weather(city)
        output = format_weather(weather_data)
        print("\n" + output)
    except Exception as e:
        print(f"❌ {e}")

if __name__ == "__main__":
    main()
