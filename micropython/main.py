# main.py -- put your code here!
# This program will make the LED lights flash on your microcontroller
# board. This works with 1st and 2nd Generation boards.

led1 = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)
while True:
    led1.toggle()
    pyb.delay(1000)
    led2.toggle()
    pyb.delay(1000)
    led3.toggle()
    pyb.delay(1000)
