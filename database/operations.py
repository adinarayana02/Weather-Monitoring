from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from .models import Base
from config.config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def init_db():
    # We don't need to create tables as they already exist in the database
    print("Database connection initialized.")

def save_weather_data(data):
    session = Session()
    try:
        session.execute(text("EXEC sp_insert_weather_data :city_name, :temp, :feels_like, :weather_condition, :datetime"),
                        {
                            "city_name": data['city'],
                            "temp": data['temp'],
                            "feels_like": data['feels_like'],
                            "weather_condition": data['main'],
                            "datetime": data['timestamp']
                        })
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def save_daily_summary(summary):
    session = Session()
    try:
        session.execute(text("EXEC sp_insert_daily_summary :city_name, :date, :avg_temp, :max_temp, :min_temp, :dominant_condition"),
                        {
                            "city_name": summary['city'],
                            "date": summary['date'],
                            "avg_temp": summary['avg_temp'],
                            "max_temp": summary['max_temp'],
                            "min_temp": summary['min_temp'],
                            "dominant_condition": summary['dominant_condition']
                        })
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def log_alert(city, message, timestamp):
    session = Session()
    try:
        session.execute(text("EXEC sp_log_alert :city_name, :alert_message, :triggered_at"),
                        {
                            "city_name": city,
                            "alert_message": message,
                            "triggered_at": timestamp
                        })
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

# Newly added function to retrieve weather data for a specific city and date
def get_weather_data_for_city_date(city, date):
    session = Session()
    try:
        result = session.execute(text("SELECT * FROM weather_data WHERE city_name = :city AND CAST(datetime AS DATE) = :date"),
                                 {"city": city, "date": date})
        return result.fetchall()  # Return the fetched weather data
    finally:
        session.close()

def get_weather_data(city, start_date, end_date):
    session = Session()
    try:
        result = session.execute(text("SELECT * FROM weather_data WHERE city_name = :city AND datetime BETWEEN :start_date AND :end_date"),
                                 {"city": city, "start_date": start_date, "end_date": end_date})
        return result.fetchall()
    finally:
        session.close()

def get_daily_summaries(city, start_date, end_date):
    session = Session()
    try:
        result = session.execute(text("SELECT * FROM daily_weather_summary WHERE city_name = :city AND date BETWEEN :start_date AND :end_date"),
                                 {"city": city, "start_date": start_date, "end_date": end_date})
        return result.fetchall()
    finally:
        session.close()
