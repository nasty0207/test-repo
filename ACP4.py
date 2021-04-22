import RPi.GPIO as GPIO
import time
 
def magic (value):
    output = 0
    if (value > 1):
        output = 1
    if (value > 32):
        output = 3
    if (value > 64):
        output = 7
    if (value > 96):
        output = 15
    if (value > 128):
        output = 31
    if (value > 160):
        output = 63
    if (value > 192):
        output = 127
    if (value > 224):
        output = 255
    return output 

outstr = "Digital value: {digital}, analog value: {analog} V"
maxV = 3.3

out_list = (26, 19, 13, 6, 5, 11, 9, 10)
led_list = (24, 25, 8, 7, 12, 16, 20, 21)
in_ch = 4
pot = 17
GPIO.setmode (GPIO.BCM)
GPIO.setup (out_list, GPIO.OUT)
GPIO.setup (led_list, GPIO.OUT)
GPIO.setup (pot, GPIO.OUT)
GPIO.setup (in_ch, GPIO.IN)
 

def decToBinList (decNumber):
    return [(decNumber & (1<<i)) >> i for i in range (7, -1, -1)]

def num2dac (value, clist):
    GPIO.output (clist, decToBinList (value))
 
def search ():
    false = 0
    tru = 255
    
    while (false < tru - 1):
        values = (false + tru) // 2
        num2dac (values, out_list)
        time.sleep (0.001)
        
        if not (GPIO.input(in_ch) == 1):
            tru = values
        else:
            false = values
    dg = false
    an = maxV * dg / 255
    print(outstr.format(digital = dg, analog = an))
    return dg 

try:
    GPIO.output (pot, 1)
    while True:
        value = search()
        num2dac(magic(value), led_list)
        time.sleep(0.1)

finally:
    GPIO.output (out_list, 0)
    GPIO.output (pot, 0)
    GPIO.cleanup (out_list)
    GPIO.cleanup (led_list)
    GPIO.cleanup (pot)
    GPIO.cleanup (in_ch)
    print('Program is finished!')