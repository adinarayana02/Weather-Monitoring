# OpenWeatherMap API configuration
API_KEY = '57fcfca14b4450e8dc2b61e4ffe103be'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Database configuration
DATABASE_URI = 'mssql+pyodbc://sa:Tadi2024@LAPTOP-K55CLBQO\\SQLEXPRESS/weather_data?driver=ODBC+Driver+17+for+SQL+Server'

# Email configuration
EMAIL_ADDRESS = 'thotaadinarayana02@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'  # For Gmail
SMTP_PORT = 587
SMTP_PASSWORD = 'fzrr pthh kdsb ebca'

# List of Indian metros
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

# Weather update interval (in seconds)
UPDATE_INTERVAL = 300  # 5 minutes

# Temperature alert threshold (in Celsius)
TEMPERATURE_THRESHOLD = 20

EMAIL_RECIPIENTS = ['adinarayanathota02@gmail.com']