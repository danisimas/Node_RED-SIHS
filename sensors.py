import paho.mqtt.client as mqtt
from random import randint
from time import sleep

def temp():
    value = randint(0,100)
    return value

def lumi ():
    value = randint(0,100)
    return value

def on_connect (client, userdata, flags, rc):
    print("Connected with result code", str(rc))
    client.subscribe("lab/sensors")

client = mqtt.Client()
client.on_connect = on_connect

# Connect to broker
client.connect('broker.hivemq.com')

# Start listening
client.loop_start()

while True:
    temp_value = temp()
    lumi_value = lumi()

    if temp_value > 25:
        client.publish("lab/airconditioner", "on")
    else:
        client.publish("lab/airconditioner", "off")
    
    if lumi_value < 50:
        client.publish("lab/lights", "on")
    else:
        client.publish("lab/lights", "off")
    sleep(1)
