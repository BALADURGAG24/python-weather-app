# 🌦 Weather App — Python GUI + Web + Auto Location

A versatile Python Weather App that works in multiple modes:

- 🖥 Desktop GUI app built with **Tkinter**
- 🌐 Web app using **Flask**
- 📍 Auto-detects user location via IP address

It fetches live weather data from **OpenWeatherMap API** and displays it in a clean, user-friendly format.

---

## ⚡ Features

- Search weather by **city name**
- Leave city blank to auto-detect location based on your IP address
- Run as a desktop **Tkinter GUI** app
- Run as a **Flask web app** accessible from browser
- Modular, clean code structure for easy maintenance

---

## 🗂 Project Structure

weather_app/
├── main.py # Optional CLI mode
├── gui_app.py # Tkinter GUI app
├── web_app.py # Flask web app
├── weather/
│ ├── init.py
│ ├── fetcher.py # API request logic
│ ├── config.py # API keys and URLs
│ └── location.py # IP-based auto-location
├── utils/
│ └── formatter.py # Weather data formatting
├── requirements.txt
└── README.md


---

## 🚀 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/HARIHARANS24/weather-app-python.git
cd weather-app-python

