from machine import Timer, Pin
# from onewire import OneWire, DS18X20
from urequests import post
from utime import sleep
from pycom import heartbeat, rgbled
# from pysense import Pysense
# from MPL3115A2 import MPL3115A2, ALTITUDE
from mqtt import MQTTClient

import gc

from config import URL, SENSOR_ID, MQTT_SERVER, MQTT_USER, MQTT_PASSWORD, \
MQTT_PORT, MQTT_PASSWORD


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

def settimeout(duration):
    pass

class Alarm:

    def __init__(self, interval):
        self.__alarm = Timer.Alarm(self.__handler, interval, periodic=True)
        # py = Pysense()
        # self.__mp = MPL3115A2(py, mode=ALTITUDE)
        self.__client = MQTTClient(SENSOR_ID, MQTT_SERVER, user=MQTT_USER,
                                        password=MQTT_PASSWORD, port=MQTT_PORT)
        self.__client.settimeout = settimeout
        self.__client.connect()

    def __handler(self, alarm):
        try:
            temperature = get_temperature("P11")
            data = {"value": str(temperature), "sensorId": SENSOR_ID}
            # data = {"value": str(self.__mp.temperature()), "sensorId": SENSOR_ID}
            print(data)
            self.__client.publish(topic="sensors/", msg="")
            # post(URL, data=data, headers={"Content-Type": "application/json"})
            gc.collect()
            gc.mem_free()
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
