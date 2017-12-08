from machine import Timer, Pin
from onewire import OneWire, DS18X20
from urequests import post
from utime import sleep
from pycom import heartbeat, rgbled

from config import URL, SENSOR_ID

def get_temperature(dat):
    # gnd = Pin(gnd, Pin.OUT, value=0)
    dat = Pin(dat)
    # vdd = Pin(vdd, Pin.OUT, value=1)
    ow = OneWire(dat)
    ds = DS18X20(ow)
    print('devices:', ds.roms)
    temp = ds.read_temps()
    print('temperatures:', temp)
    return temp[0]

class Alarm:

    def __init__(self, interval):
        self.__alarm = Timer.Alarm(self.__handler, interval, periodic=True)

    def __handler(self, alarm):
        try:
            temperature = get_temperature("P11")
            data = {"value": temperature, "sensorId": SENSOR_ID}
            # post(URL, data=data, headers={"Content-Type": "application/json"})
            post(URL, json=data)
            print('sent')
            rgbled(0x00ff00)
            sleep(1)
            rgbled(0x000000)

        except Exception as e:
            rgbled(0xff0000)
            sleep(1)
            rgbled(0x000000)
            sleep(1)
            rgbled(0xff0000)
            sleep(1)
            rgbled(0x000000)
            print("error %s" % e)
            pass

    def stop(self):
        self.__alarm.callback(None)
