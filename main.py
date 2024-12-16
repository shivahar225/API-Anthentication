import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWN_ENDpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWN_API_KEY")
account_sid = "AC71ee7178dc28f82faa6a4775cc6a94ba"
auth_token = "052a077d995aa178c146c2cd075a1b10"

weather_params = {
    "lat": 51.759048,
    "lan": 19.458599,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_ENDpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    if will_rain:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'http': os.environ['https_proxy']}

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to="+919705644653",
            body="it's going to rain today. remember to bring umbrella",
            from_="+9195735945543"
                    )
        print(message.sid)
