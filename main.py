from pycom import heartbeat, rgbled
from alarm import Alarm

heartbeat(False)
alarm = Alarm(15*60)


# while True:
#     try:
#         temperature = get_temperature("P11")
#         data = {"value": temperature, "sensorId": SENSOR_ID}
#         # post(URL, data=data, headers={"Content-Type": "application/json"})
#         post(URL, json=data)
#         print('sent')
#         rgbled(0x00ff00)
#         sleep(1)
#         rgbled(0x000000)

#     except Exception as e:
#         rgbled(0xff0000)
#         sleep(1)
#         rgbled(0x000000)
#         sleep(1)
#         rgbled(0xff0000)
#         sleep(1)
#         rgbled(0x000000)
#         print("error %s" % e)
#         pass

#     sleep(60*10)
