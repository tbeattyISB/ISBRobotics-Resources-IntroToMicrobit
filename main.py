from microbit import *


def prog1():
    display.show(Image.HEART)
    pass


def prog2():
    display.show(Image.HAPPY)
    pass


def prog3():
    display.show(Image.SAD)
    pass


def prog4():
    display.show(Image.ANGRY)
    pass


choice = 1
programs = [prog1, prog2, prog3, prog4]


while True:
    display.clear()
    display.set_pixel(choice - 1, 0, 9)  # show the chosen program
    if button_a.was_pressed():
        if choice < 4:
            choice = choice + 1
        else:
            choice = 1
    if button_b.was_pressed():
        programs[choice - 1]()  # run the chosen program
        sleep(2000)
