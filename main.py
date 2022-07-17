import requests

from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

api = "ba65fe6e9e736b2bc8abee49d1971c3e"
account_sid = "AC0df5f99ac5f7fb2396ac877b3a3b22a4"
auth_token = "5dabc2734f3236ae365c5d2cb3af5ef0"

wether_Params = {
    "lat": 18.520760,
    "lon": 73.855408,  # pune
    "appid": api,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=wether_Params)
response.raise_for_status()
# print(response.status_code)

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella.",
        from_="+14142400638",
        to="+917620169960"
    )
    print(message.status)

# #print("Bring an Umbrella.")
# #print(weather_slice)
# #print(weather_data["hourly"][0]["weather"])
