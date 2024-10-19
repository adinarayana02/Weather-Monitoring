import smtplib
from email.mime.text import MIMEText
from config.config import EMAIL_ADDRESS, SMTP_SERVER, SMTP_PORT, SMTP_PASSWORD


def send_alert_email(recipients, city, temperature):
    subject = f"🌡️ Weather Alert: High Temperature in {city}"

    body = f"""
    <html>
        <body>
            <h2>Weather Alert for {city}</h2>
            <p>The temperature in <strong>{city}</strong> has exceeded the threshold.</p>
            <p>Current temperature: <strong>{temperature:.2f}°C</strong></p>
            <p>Please take the necessary precautions.</p>
            <p>Best Regards,<br>Your Weather Monitoring System</p>
        </body>
    </html>
    """

    msg = MIMEText(body, 'html')  # Create a MIMEText object with HTML format
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ", ".join(recipients)  # Join multiple recipients with a comma

    try:
        # Establish a secure SMTP connection
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, SMTP_PASSWORD)  # Log in to the email server
            server.send_message(msg)  # Send the email
        print(f"Alert email sent successfully to {', '.join(recipients)}")  # Success message
    except Exception as e:
        print(f"Failed to send email: {e}")  # Error handling

# Example usage
# send_alert_email(['recipient1@example.com', 'recipient2@example.com'], 'Delhi', 40.5)
