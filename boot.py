# boot.py -- run on boot-up
import os
from machine import UART, reset_cause, SOFT_RESET
from pycom import heartbeat, rgbled
from utime import sleep
from wlan import setup_wifi


uart = UART(0, 115200)
os.dupterm(uart)

heartbeat(False)
rgbled(0x0000aa)
sleep(3)
rgbled(0x000000)
sleep(1)
rgbled(0x0000aa)
sleep(3)
rgbled(0x000000)

if reset_cause() != SOFT_RESET:
    setup_wifi()
