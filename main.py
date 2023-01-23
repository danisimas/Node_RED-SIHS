from ctypes.wintypes import MSG
import paho.mqtt.client as mqtt
from random import randint
from time import sleep

def on_connect (client, userdata, flags, rc):
    print("Connected with result code", str(rc))
    client.subscribe("lab/airconditioner")
    client.subscribe("lab/lights")

    try:
        current_luminosity = int(MSG.payload)
        client.publish("/lab/sensorLum", "ligar" if current_luminosity <= 40 else "desligar")

    except:
        pass
    
client = mqtt.Client()
client.on_connect = on_connect



# Connect to broker
client.connect('broker.hivemq.com')

# Start listening
client.loop_forever()