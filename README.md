
# Real-Time Weather Monitoring System

This project is a **Real-Time Weather Monitoring System** that retrieves weather data for major Indian metros using the **OpenWeatherMap API**, stores it in a **Microsoft SQL Server database**, and triggers email alerts when specific temperature thresholds are breached. The system is built with Python and employs various modules for data retrieval, processing, alerting, and visualization.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Modules and Explanation](#modules-and-explanation)
  - [API Configuration](#api-configuration)
  - [Database Configuration](#database-configuration)
  - [Email Configuration](#email-configuration)
- [Step-by-Step Process](#step-by-step-process)
- [Usage](#usage)
- [Visualization](#visualization)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Real-time weather data retrieval for Indian metro cities.
- Data storage using **Microsoft SQL Server**.
- Daily summaries and aggregation of weather data.
- Email alerts for high-temperature thresholds.
- Visualization of weather trends.
  
---

## Project Structure

```bash
├── config.py            # Configuration settings for API, database, email
├── models.py            # SQLAlchemy models for database tables
├── operations.py        # Database operations (CRUD)
├── email_service.py     # Email alerting service
├── weather_service.py   # Weather data retrieval and processing
├── utils.py             # Utility functions (data validation, conversions, etc.)
├── plot.py              # Visualization using matplotlib/plotly
└── main.py              # Main script to run the entire system
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/adinarayana02/weather-monitoring.git
cd weather-monitoring
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

Make sure to install libraries for database management, requests, and email handling.

### 3. Configure Environment Variables

You’ll need to configure your **API key**, **database credentials**, and **email details**. Update the `config.py` file with your values.

```python
# config.py

API_KEY = '57fcfca14b4450e8dc2b61e4ffe103be'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Database configuration
DATABASE_URI = 'mssql+pyodbc://sa:Tadi2024@LAPTOP-K55CLBQO\\SQLEXPRESS/weather_data?driver=ODBC+Driver+17+for+SQL+Server'


# Email configuration
EMAIL_ADDRESS = 'thotaadinarayana02@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_PASSWORD = 'fzrr pthh kdsb ebca'
EMAIL_RECIPIENTS = ['recipient1@example.com', 'recipient2@example.com']

# General settings
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
UPDATE_INTERVAL = 300  # In seconds (5 minutes)
TEMPERATURE_THRESHOLD = 20  # Temperature threshold for alerts
```

### 4. Set Up SQL Server Database

Create the `weather_data` table in SQL Server by running the `models.py` script. It sets up the necessary table to store weather data.

```bash
python models.py
```

### 5. Run the Application

To start the weather monitoring system, run the `main.py` file:

```bash
python main.py
```

This script will continuously fetch weather data, store it in the database, check for temperature alerts, and send emails when necessary.

---

## Modules and Explanation

### API Configuration

The weather data is retrieved using the **OpenWeatherMap API**. The `config.py` file holds the API key and base URL.

### Database Configuration

The application uses **SQLAlchemy** with **Microsoft SQL Server** for storing and retrieving weather data. All database interactions are handled in `operations.py`.

### Email Configuration

Email notifications for weather alerts are configured using **Gmail's SMTP** server. The `email_service.py` handles email sending when temperature thresholds are exceeded.

---

## Step-by-Step Process

1. **Weather Data Retrieval:**
   - The system fetches weather data for the cities listed in `config.py` using the OpenWeatherMap API.
   - Each request retrieves data such as temperature, weather conditions, and humidity.

2. **Data Processing:**
   - The weather data is processed using the `weather_service.py`, where it's formatted for database insertion.

3. **Database Storage:**
   - The processed data is stored in the `weather_data` table using SQLAlchemy models from `models.py`.

4. **Temperature Alerts:**
   - The system checks if the current temperature exceeds the `TEMPERATURE_THRESHOLD`. If true, it triggers the `email_service.py` to send an alert.

5. **Daily Summary and Aggregation:**
   - At the end of each day, the system aggregates daily weather data for each city and calculates metrics like average, max, and min temperatures, which can be visualized using `plot.py`.

6. **Real-Time Loop:**
   - The `main.py` script runs a loop that fetches data at regular intervals (5 minutes), stores it in the database, and checks for alerts.

---

## Usage

- To **customize cities** or modify the **alert threshold**, update the values in `config.py`.
- You can retrieve daily summaries or run custom SQL queries using `operations.py`.
  
---

## Visualization

For visualizing weather trends, the project includes a `plot.py` script, which uses **matplotlib** or **plotly**. You can generate graphs for daily temperature, weather conditions, or historical trends by running:

```bash
python plot.py
```

Example visualization:

- **Average Temperature vs. Time**
- **Temperature Variations for Major Cities**

---

## Testing

### Unit Testing with Pytest

You can run unit tests using **pytest**. Make sure you have mock API responses and mock database connections for isolated tests.

```bash
pytest tests/
```

- Test **weather retrieval** functions to ensure they handle various scenarios (e.g., valid city, invalid city, API failure).
- Test **database operations** to ensure data is inserted and retrieved correctly.
- Test the **email alert** system to verify alerts are sent when the threshold is exceeded.

---

## Contributing

Contributions are welcome! Please create a pull request or raise an issue if you'd like to contribute or report bugs. Make sure to follow coding conventions and thoroughly test any changes.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

### Author

- [Adinarayana Thota](https://github.com/adinarayana02)

---
