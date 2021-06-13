import paho.mqtt.client as mqtt
import time

client = mqtt.Client("Publisher")  # создание клиента

client.connect("127.0.0.1", 1883, 60)  # подключение к брокеру
client.loop_start()  # start the loop


step = 1
while True:
    if step == 1:
        for i in range(11):
            step = i

            coord = "coord,host=sensors value="+str(i)
            client.publish("sensors", coord)
            print(coord)
            time.sleep(1)
    elif step == 10:
        for i in range(step-1, 0, -1):
            step = i
            coord = "coord,host=sensors value="+str(i)
            client.publish("sensors", coord)
            print(coord)
            time.sleep(1)
