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
    client.publish("lab/airconditioner", temp_value)
    client.publish("lab/lights", lumi_value)
    sleep(1)
