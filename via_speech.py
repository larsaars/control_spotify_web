from time import sleep
from typing import Union

import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()


def recognize() -> Union[str, None]:
    with mic as src:
        recognizer.adjust_for_ambient_noise(src)
        audio = recognizer.listen(src)

    try:
        return recognizer.recognize_google(audio, language='en-US')
    except sr.UnknownValueError or sr.UnknownValueError:
        return None


if __name__ == '__main__':
    while True:
        sleep(0.2)

        print('recording...')
        res = recognize().lower().strip()

        if ('music' in res) and ('play' in res):
            print('playing music')