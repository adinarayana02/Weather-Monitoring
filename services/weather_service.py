import requests
from datetime import datetime, timedelta
from database.operations import save_weather_data, save_daily_summary, log_alert, get_weather_data
from config.config import BASE_URL, API_KEY


def fetch_weather_data(city):
    """Fetch weather data from the weather API."""
    response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})

    if response.status_code != 200:
        raise Exception(f"Error fetching weather data: {response.status_code}")

    return response.json()


def process_weather_data(city):
    """Process and save the weather data for a given city."""
    data = fetch_weather_data(city)

    # Constructing the data to be saved in the database
    weather_data = {
        'city': data['name'],
        'temp': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'main': data['weather'][0]['main'],
        'timestamp': datetime.now()
    }

    # Save weather data to the database
    save_weather_data(weather_data)

    # Return processed data
    return weather_data


def calculate_daily_summary(city, date):
    """Calculate and save the daily summary for a given city and date."""
    start_date = datetime.combine(date, datetime.min.time())
    end_date = datetime.combine(date, datetime.max.time())

    # Fetch weather data for the day
    records = get_weather_data(city, start_date, end_date)

    if records:
        avg_temp = sum(record[2] for record in records) / len(records)  # Ensure the right index for temperature
        max_temp = max(record[2] for record in records)  # Ensure the right index for temperature
        min_temp = min(record[2] for record in records)  # Ensure the right index for temperature
        dominant_condition = max(set(record[3] for record in records), key=[record[3] for record in records].count)  # Adjust as needed

        daily_summary = {
            'city': city,
            'date': date,
            'avg_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        }

        # Save daily summary to the database
        save_daily_summary(daily_summary)



def check_alert_threshold(data, threshold):
    """Check if the current temperature exceeds the threshold for alerts."""
    return data['temp'] > threshold


def log_weather_alert(city, temp):
    """Log a weather alert for the city."""
    message = f"Temperature alert! {temp}°C in {city} exceeds the threshold."
    timestamp = datetime.now()
    log_alert(city, message, timestamp)
