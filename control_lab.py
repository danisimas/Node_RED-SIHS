import paho.mqtt.client as mqtt
import json

# Callback function to handle incoming messages
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    temperature = data['temperature']
    light = data['light']
    
    if temperature > 25:
        client.publish("/dn/danynatan/airconditioner", "on")
    else:
        client.publish("/dn/danynatan/airconditioner", "off")
    
    if light < 50:
        client.publish("/dn/danynatan/lights", "on")
    else:
        client.publish("/dn/danynatan/lights", "off")

# Create MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect to broker
client.connect("broker.hivemq.com")

# Subscribe to topic
client.subscribe("/dn/danynatan/sensor")

# Start listening
client.loop_forever()
