import requests
import os
from twilio.rest import Client
import smtplib

#Api key="80fbbacf7e5f38809d0947ba03c0d7d8"

account_sid = 'ACd89799b5bd8acf417939625704bad684'
auth_token = '787ca08ce83cc4a1f796a95b836ff9d9'

user = "mehul.jainudemy@gmail.com"
password = "mehul1234 "


parameter={
    "lat":25.317644,
    "lon":82.973915,
    "appid":"80fbbacf7e5f38809d0947ba03c0d7d8",
    "exclude":"current,minutely,daily",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice=weather_data["hourly"][:12]

will_rain=False

for hour_data in weather_slice:
    condition=hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=user,password=password)
    connection.sendmail(from_addr=user,to_addrs=user,msg="subject:It rain today\n\n Plaese Bring Your umbrella")

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+12018905753',
        to='+91 95280 27068'
    )

    print(message.status)

