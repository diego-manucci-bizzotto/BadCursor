import datetime
import random
import time
import autoit
import keyboard
import requests

url = 'https://badcursor.onrender.com/actions'


def tremer():
    time_to_stop = datetime.datetime.now() + datetime.timedelta(seconds=2.5)
    while datetime.datetime.now() < time_to_stop:
        time.sleep(0.001)
        x_movement = random.randint(-5, 5)
        y_movement = random.randint(-5, 5)
        autoit.mouse_move(autoit.mouse_get_pos()[0] + x_movement, autoit.mouse_get_pos()[1] + y_movement, 5)


def congelar():
    time_to_stop = datetime.datetime.now() + datetime.timedelta(seconds=5)
    pos = autoit.mouse_get_pos()
    while datetime.datetime.now() < time_to_stop:
        autoit.mouse_move(pos[0], pos[1], 0)


def alttab():
    keyboard.press_and_release('alt+tab')


def run():
    while True:
        time.sleep(5)
        response = requests.get(url)
        print(response.json())
        actions = response.json()
        if response.status_code == 200 and len(actions) > 0:
            action = actions[0]
            if action == 'tremer':
                tremer()
            elif action == 'congelar':
                congelar()
            elif action == 'alttab':
                alttab()


if __name__ == "__main__":
    run()
