from pyautogui import typewrite, press
from time import sleep

def rrg():
    message = input('ENTER THE TEXT: ')
    number = int(input('HOW MUCH = '))
    slep = int(input('HOW MUCH I SHOULD WAIT = '))

    sleep(slep)

    tw = typewrite
    pr = press

    for i in range(number):
        tw(message)
        pr('enter')
        sleep(0.01)

    print("DONE")

rrg()
