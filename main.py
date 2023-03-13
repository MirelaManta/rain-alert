import os
import requests
from twilio.rest import Client

# API Authentication

# API Key ---> a way to prevent people from abusing their(an API provider's) service
# Through API Key the API provider can track how much you're using
# their API and to authorize your access or deny your access once you've got over the limit

api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
account_sid = "ACe7989eb689c398b1a99fb0fc03fec53a"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 44.426765,    # Bucharest
    "lon": 26.102537,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}
response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
wd_12_hours = weather_data["hourly"][:12]   # the weather forecast for the next 12 hours

will_rain = False

condition_codes = [hour_data["weather"][0]["id"] for hour_data in wd_12_hours]

for code in condition_codes:
    if int(code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️.",
        from_="+15747014188",
        to="+40 784596521"  # Not my actual number, you need to provide a valid number and verify it.
        )
    print(message.status)


# Twilio is an API service that allows us to send text messages or phone calls
# or have a virtual phone number in any country


# Environment variables
# What are they used for? There is two major use cases. One is for convenience. Second reason might be for security.
# Environment variables allow us to separate out where we store our keys, our secret stuff
# and various others variables away from where our code base is located.
