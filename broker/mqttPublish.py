import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import json
from datetime import datetime



mqttBroker = "localhost"
client = mqtt.Client("temp")
client.connect(mqttBroker, 1883)

message = json.loads('{"timestamp": "2023-12-23 13:10:00","sensor": "temperature","value": 30}')


while True :
    randNumber = uniform(10.0, 20.0)
    message["value"] = randNumber
    message["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client.publish("temperature", json.dumps(message))
    print("just published ", str(message), "to Topic temprature")
    time.sleep(5)
