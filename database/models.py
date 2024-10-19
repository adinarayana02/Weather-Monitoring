from sqlalchemy import Column, Integer, String, Float, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base

# Initialize the base class for SQLAlchemy models
Base = declarative_base()

# Model for the 'weather_data' table
class WeatherData(Base):
    __tablename__ = 'weather_data'

    # Columns for storing weather data
    id = Column(Integer, primary_key=True)
    city_name = Column(String(100), nullable=False)
    temp = Column(Float, nullable=False)
    avg_temp = Column(Float, nullable=False)
    min_temp = Column(Float, nullable=False)
    max_temp = Column(Float, nullable=False)
    feels_like = Column(Float, nullable=False)
    weather_condition = Column(String(50), nullable=False)
    datetime = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<WeatherData(city_name={self.city_name}, temp={self.temp}, feels_like={self.feels_like}, weather_condition={self.weather_condition}, datetime={self.datetime})>"

# Model for the 'daily_weather_summary' table
class DailyWeatherSummary(Base):
    __tablename__ = 'daily_weather_summary'

    # Columns for storing daily summary data
    id = Column(Integer, primary_key=True)
    city_name = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)
    avg_temp = Column(Float, nullable=False)
    max_temp = Column(Float, nullable=False)
    min_temp = Column(Float, nullable=False)
    dominant_condition = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<DailyWeatherSummary(city_name={self.city_name}, date={self.date}, avg_temp={self.avg_temp}, max_temp={self.max_temp}, min_temp={self.min_temp}, dominant_condition={self.dominant_condition})>"

# Model for the 'weather_alerts' table
class WeatherAlert(Base):
    __tablename__ = 'weather_alerts'

    # Columns for storing weather alerts
    id = Column(Integer, primary_key=True)
    city_name = Column(String(100), nullable=False)
    alert_message = Column(String(255), nullable=False)
    triggered_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<WeatherAlert(city_name={self.city_name}, alert_message={self.alert_message}, triggered_at={self.triggered_at})>"
