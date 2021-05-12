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
    cmd = 'espeak -ven+f6 -k5 -s150 -s94 -a %s --punct="<characters>" "%s" 2 >> /dev/null' % ('21', inp)
    execute_unix(cmd)


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


def say_weather_tomorrow_extra():
    json = requests.get(
        f'https://api.openweathermap.org/data/2.5/forecast?q={CITY_NAME}&appid={OWM_API_KEY}&lang={LANGUAGE}&units=metric&cnt=8').json()
    out = 'The detailed weather for the next 24 hours. '

    for item in json['list']:
        out += f'At {get_time(item["dt"])} it has {item["main"]["temp"]} degrees with {item["weather"][0]["description"]}. '

    out += f'The sun sets at {get_time(json["city"]["sunset"])}'

    say(out)


def say_weather_tomorrow_short():
    json = requests.get(
        f'https://api.openweathermap.org/data/2.5/forecast?q={CITY_NAME}&appid={OWM_API_KEY}&lang={LANGUAGE}&units=metric&cnt=8').json()

    for item in json['list']:
        timestamp = get_time(item["dt"])
        if timestamp == '15:00 o\'clock' or timestamp == '14:00 o\'clock' or timestamp == '13:00 o\'clock':
            say(f'Tomorow, at {timestamp} it will have {item["main"]["temp"]} degrees with {item["weather"][0]["description"]}. The wind speed will be {item["wind"]["speed"]} kilometres per hour.')
            break


def say_weather_next_days():
    json = requests.get(
        f'https://api.openweathermap.org/data/2.5/forecast?q={CITY_NAME}&appid={OWM_API_KEY}&lang={LANGUAGE}&units=metric').json()
    out = 'The weather for the next days. '

    for item in json['list']:
        timestamp = get_time(item['dt'])
        if timestamp == '15:00 o\'clock' or timestamp == '14:00 o\'clock' or timestamp == '13:00 o\'clock':
            extra_timestamp = datetime.fromtimestamp(item['dt']).strftime('On %d.%m. at %H:%M o\'clock')
            out += f'{extra_timestamp} it will have {item["main"]["temp"]} degrees with {item["weather"][0]["description"]}. '

    say(out)
