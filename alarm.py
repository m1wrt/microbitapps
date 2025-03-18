# Imports go at the top
from microbit import *

#18/03/2025

# Code in a 'while True:' loop repeats forever
while True:
    pin0.write_digital()
    if pin14.read_digital() == 1:
            display.show(Image.ARROW_N)
            pin0.write_digital(1)
            sleep(1000)
            pin0.write_digital(0)
            sleep(1000)
            pin1.write_digital(1)
            sleep(1000)
            pin1.write_digital(0)
            sleep(1000)
            pin2.write_digital(1)
            sleep(1000)
            pin2.write_digital(0)
            sleep(1000)


            
    if pin13.read_digital() == 1:
            display.show(Image.ARROW_S)
            pin2.write_digital(1)
            sleep(1000)
            pin2.write_digital(0)
            sleep(1000)
            pin1.write_digital(1)
            sleep(1000)
            pin1.write_digital(0)
            sleep(1000)
            pin0.write_digital(1)
            sleep(1000)
            pin0.write_digital(0)
            sleep(1000)


    else:
            display.show(Image.ANGRY)
            pin0.write_digital(0)
            pin1.write_digital(0)
            pin2.write_digital(0)

            
