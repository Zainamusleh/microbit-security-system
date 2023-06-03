# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats foreverpin
while True :
    if pin2.read_digital==1:
        pin1.write_digital(1)
        pin0.write_digital(1)
    elif pin2.read_digital==0:
        pin1.write_digital(0)
        pin0.write_digital(0)