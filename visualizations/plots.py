import matplotlib.pyplot as plt
from database.operations import get_daily_summaries
from datetime import datetime, timedelta


def plot_temperature_trend(city, days=7):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    summaries = get_daily_summaries(city, start_date, end_date)

    dates = [summary.date for summary in summaries]
    avg_temps = [summary.avg_temp for summary in summaries]
    max_temps = [summary.max_temp for summary in summaries]
    min_temps = [summary.min_temp for summary in summaries]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, avg_temps, label='Average')
    plt.plot(dates, max_temps, label='Max')
    plt.plot(dates, min_temps, label='Min')
    plt.title(f'Temperature Trend for {city} (Last {days} Days)')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{city}_temperature_trend.png')
    plt.close()


def plot_weather_distribution(city, days=7):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    summaries = get_daily_summaries(city, start_date, end_date)

    conditions = [summary.dominant_condition for summary in summaries]
    condition_counts = {}
    for condition in conditions:
        condition_counts[condition] = condition_counts.get(condition, 0) + 1

    plt.figure(figsize=(8, 8))
    plt.pie(condition_counts.values(), labels=condition_counts.keys(), autopct='%1.1f%%')
    plt.title(f'Weather Distribution for {city} (Last {days} Days)')
    plt.savefig(f'{city}_weather_distribution.png')
    plt.close()