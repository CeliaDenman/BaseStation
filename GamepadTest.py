__author__ = 'Danny'

import time
import pygame
pygame.init()
pygame.joystick.init()
done = False

joystick = pygame.joystick.Joystick(0)
joystick.init()

def getJoyVal( axis ):
    "this function returns the value of a joystick, given an axis and a joystick number"
    value = joystick.get_axis(axis)
    return value

while done==False:
    pygame.event.get()


    print getJoyVal(0)
    print getJoyVal(1)
    time.sleep(.5)