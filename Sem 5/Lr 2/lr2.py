import requests
import json

def get_weather_data(place:str, api_key=''):
    req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ place + '&appid=' + api_key)
    res = json.loads(req.text)
    feels_like = round(res['main']['feels_like'] - 273.15, 2)
    if res['timezone'] < 0:
        timezone = 'UTC'+str(round(res['timezone'] / 3600))
    else:
        timezone = 'UTC+'+str(round(res['timezone'] / 3600))
    result = {"name": res['name'], "coord": res['coord'], "country": res['sys']['country'], "feels_like": feels_like, "timezone": timezone}
    return json.dumps(result)

print(get_weather_data("Санкт-Петербург", 'afbcb1e5d0091123e1da60085ac48f21'))