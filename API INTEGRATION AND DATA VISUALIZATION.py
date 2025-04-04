import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime

 
API_KEY = "88f004ecf4f0cecb25dc6f830ba18ab2"   
CITY = "London"   
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

 
def get_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

 
weather_data = get_weather_data(CITY)

if weather_data:
     
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    pressure = weather_data["main"]["pressure"]
    wind_speed = weather_data["wind"]["speed"]
    weather_desc = weather_data["weather"][0]["description"]
    
     
    data = {
        "Metric": ["Temperature", "Feels Like", "Humidity", "Pressure", "Wind Speed"],
        "Value": [temp, feels_like, humidity, pressure, wind_speed],
        "Unit": ["°C", "°C", "%", "hPa", "m/s"]
    }
    df = pd.DataFrame(data)

     
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df["Metric"], df["Value"])
    
     
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}',
                ha='center', va='bottom')
    
    plt.title(f"Current Weather in {CITY} - {weather_desc}")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

     
    plt.figure(figsize=(10, 6))
    sns_plot = sns.barplot(data=df, x="Metric", y="Value", palette="viridis")
    
     
    for i in sns_plot.containers:
        sns_plot.bar_label(i, fmt='%.1f')
    
    plt.title(f"Current Weather Conditions in {CITY}")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

     
    print(f"\nWeather in {CITY} on {datetime.now().strftime('%Y-%m-%d')}:")
    print(f"Temperature: {temp}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure}hPa")
    print(f"Wind Speed: {wind_speed}m/s")
    print(f"Conditions: {weather_desc}")
else:
    print("Failed to fetch weather data")
