import RPi.GPIO as GPIO
import time 
import numpy as np

GPIO.setmode(GPIO.BCM)
#GPIO.setup(24,GPIO.OUT)
chan_list = [24, 25, 8, 7, 12, 16, 20, 21]
for i in chan_list:
    GPIO.setup(i,GPIO.OUT)

def lightUp(ledNumber, period):
    ledNumber = chan_list[ledNumber]
    GPIO.output(ledNumber, 1)
    time.sleep (period)
    GPIO.output(ledNumber, 0)

def lightOff(ledNumber, period):
    #ledNumber = chan_list[ledNumber]
    GPIO.output(ledNumber, 0)
    time.sleep (period)
    GPIO.output(ledNumber, 1)


def blink(ledNumber, blinkCount, blinkPeriod):
    for j in range(blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)

def runningLight (count, period):
    for j in range(count):
        for i in chan_list:
            lightUp(i, period)

def runningDark (count, period):
    GPIO.output (chan_list, 1)
    for j in range(count):
        for i in chan_list:
            lightOff(i, period)
    GPIO.output (chan_list, 0)
    GPIO.cleanup(chan_list)


def decToBinList(decNumber):
    binNumber = np.zeros(8)
    for j in range(8):
        binNumber[j] = decNumber % 2
        decNumber /= 2
    return reverse (binNumber, 8)

def reverse (arr, n):
    r_arr = np.zeros (n)
    for i in range (n):
        r_arr[i] = arr[n - i - 1]
    return r_arr 

def lightNumber(number):
    GPIO.output (chan_list, 0)
    registers = decToBinList(number)
    for j in range(8):
        if (registers[7 - j] == 1):
            GPIO.output (chan_list[j], 1)
            GPIO.cleanup(chan_list)


def runningPattern (pattern, direction):
    GPIO.output(chan_list, 0)
    arr = decToBinList(pattern)
    array = [0]* 8
    for t in range(0, 9):
        for i in range(0, 8):
            array[i] = arr[(i + t*direction)  % 8]
        for j in range(0,8):
            if (array[7 - j] == 1):
                GPIO.output(chan_list[j], 1)
        time.sleep(1)
        GPIO.output (chan_list, 0)


def SlowMotion(ledNumber, count):
    p = GPIO.PWM(chan_list[ledNumber], 50)
    p.start(0)
    for i in range (count):
        for dc in range (0,101,5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        for dc in range (100,-1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)

    p.stop()

#GPIO.cleanup (chan_list)



    




#lightUp (3 ,2)
#blink (3, 3, 0.1)
#lightOff (chan_list[3],1)
#runningLight (2,0.1)
#runningDark(2, 0.1)
#print (decToBinList(3))
#lightNumber (133)
#runningPattern(6,1)
SlowMotion (3,2)