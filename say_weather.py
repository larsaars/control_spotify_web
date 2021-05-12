import subprocess
from datetime import datetime

import requests

from config import CITY_NAME, LANGUAGE

with open('owm_api_key.txt', 'r') as f:
    OWM_API_KEY = f.readline()


# execute cmd in unix
def execute_unix(input_command: str):
    p = subprocess.Popen(input_command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    return output


# timestamp to say-able string
def get_time(timestamp) -> str:
    return datetime.fromtimestamp(int(timestamp)).strftime('%H:%M o\'clock')


# say sth via tts
def say(inp: str):
    cmd = 'espeak -ven+f4 -k5 -s150 -a %s --punct="<characters>" "%s" 2 >> /dev/null' % ('30', inp)
    # execute_unix(cmd)
    print(inp)


# say weather functions
def say_sunrise_set():
    json = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={OWM_API_KEY}&lang={LANGUAGE}&units=metric').json()
    say(f'The sun rises at {get_time(json["sys"]["sunrise"])} and sets at {get_time(json["sys"]["sunset"])} today.')


# say weather functions
def say_weather_now():
    json = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={OWM_API_KEY}&lang={LANGUAGE}&units=metric').json()
    say(f'It currently has {json["main"]["temp"]} degrees celsius with {json["weather"][0]["description"]}. The wind speed is {json["wind"]["speed"]} kilometres per hour.')
