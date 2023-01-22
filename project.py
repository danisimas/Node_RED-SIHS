from paho.mqtt import client as mqtt
from random import randint

def temp_manager():
    value = randint(0, 100)
    return value

def lum_manager():
    value = randint(0, 100)
    return value

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

