#!/usr/bin/python2
#
# Move the robot forwards and backwards
from romipi_astar.romipi_driver import AStar
import time

romi = AStar()
linear_ms = 0.0
rotate_rads = 0.0

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def print_instructions():
    print ("press a to move in circle, b for square")

# all set up, now run the robot
print_instructions()
while True:
    c = getch()
    if c.upper() == 'A': # circle
        for i in range(80):
                romi.circle()
    elif c.upper() == 'B': # square
        for i in range (1):
                romi.square()
    elif c.upper() == 'Z': # halt
        romi.twist(0.0, 0.0)
    elif c.upper() == 'I':
        romi.print_debug_info()
    elif c.upper() == 'Q':
        break
    else:
        print_instructions()
        continue
# stop motors and shut down light
romi.twist(0.0, 0.0)
romi.pixels(0, 0, 0)


