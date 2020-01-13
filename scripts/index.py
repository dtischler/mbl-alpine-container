import qwiic
import time
import gps
import json
import paho.mqtt.client as mqtt
from datetime import datetime

import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("iot-weather")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client, userdata, mid):
    print("Message Publisted "+str(mid))

def on_log(mqttc, obj, level, string):
    print(string)

mqttclient = mqtt.Client()
mqttclient.on_log = on_log
mqttclient.on_connect = on_connect
mqttclient.on_message = on_message
mqttclient.on_publish = on_publish
mqttclient.username_pw_set("device", password="insert-password-here")
mqttclient.loop_start()
mqttclient.connect("insert-fqdn-of-server-here", 3883, 60)

CCS811 = qwiic.QwiicCcs811()
BME280 = qwiic.QwiicBme280() 

CCS811.begin()
BME280.begin()

coordinates = gps.getCoordinates()
latitude = coordinates[0]
longitude = coordinates[1]

tags = {
    # TODO set the device ID to be a unique ID
    "deviceId": "device-123", 
    "latitude": latitude,
    "longitude": longitude,
    "synced": False,
}

# Wait for device to warm up before reading data.
time.sleep(10)

while True:
    try:
        CCS811.read_algorithm_results()
        date = datetime.utcnow().isoformat(' ')
        
        json_body = [
            {
                "measurement": "CO2",
                "tags": tags,
                "time": date,
                "fields": {
                    "value": CCS811.CO2,
                },
            },
            {
                "measurement": "tVOC",
                "tags": tags,
                "time": date,
                "fields": {
                    "value": CCS811.TVOC,
                },
            },
            {
                "measurement": "fahrenheit",
                "tags": tags,
                "time": date,
                "fields": {
                    "value": BME280.get_temperature_fahrenheit(),
                },
            },
            {
                "measurement": "celsius",
                "tags": tags,
                "time": date,
                "fields": {
                    "value": BME280.get_temperature_celsius(),
                },
            },
            {
                "measurement": "pressure",
                "tags": tags,
                "time": date,
                "fields": {
                    "value": BME280.pressure,
                },
            },
            {
                "measurement": "humidity",
                "tags": tags,
                "time": date,
                "fields": {
                    "value": BME280.humidity,
                },
            },
        ]

        res = mqttclient.publish("iot-weather", payload=json.dumps(json_body), qos=2)
        time.sleep(60)
    except Exception as err:
        print("An error occurred. Error details:")
        print(err.args)
        time.sleep(60)
