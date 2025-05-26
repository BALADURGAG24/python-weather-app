import tkinter as tk
from tkinter import messagebox
from weather.fetcher import get_weather
from weather.location import get_location_city
from utils.formatter import format_weather

def fetch_weather():
    city = city_entry.get().strip()
    if not city:
        city = get_location_city()
        if not city:
            messagebox.showerror("Error", "Could not detect location.")
            return
    try:
        data = get_weather(city)
        result = format_weather(data)
        output_label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter City (leave blank to auto-detect):").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=fetch_weather).pack(pady=10)

output_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
output_label.pack(pady=10)

root.mainloop()
