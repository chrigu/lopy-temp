from network import WLAN
from utime import sleep
from pycom import rgbled

from config import SSID, WLAN_PW, IP_CONFIG

def wait_for_connection(wifi, timeout=10):
    while not wifi.isconnected() and timeout > 0:
        sleep(1)
        timeout -= 1
    if wifi.isconnected():
        rgbled(0x00ff00)
        sleep(1)
        rgbled(0x000000)
        sleep(1)
        rgbled(0x00ff00)
        sleep(1)
        rgbled(0x000000)
        print('Connected')
    else:
        rgbled(0xaa0000)
        sleep(2)
        rgbled(0x000000)
        sleep(1)
        rgbled(0xaa0000)
        sleep(2)
        rgbled(0x000000)
        print('Connection failed!')


def setup_wifi():
    # setup as a station
    wlan = WLAN(mode=WLAN.STA)

    wlan.scan()     # scan for available networks
    wlan.ifconfig(config=IP_CONFIG)
    wlan.connect(SSID, auth=(WLAN.WPA2, WLAN_PW),  timeout=10000)

    rgbled(0xf00f00)
    wait_for_connection(wlan)
    rgbled(0x0f000f)
    # wlan.ifconfig(config='dhcp')
    # wait_for_connection(wlan)

    print(wlan.ifconfig())
