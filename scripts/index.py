import qwiic
import time
import logging
import gps
from influxdb import InfluxDBClient
from datetime import datetime

# Wait for influxd to start up.
time.sleep(10)

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('iot-weather')

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

    print("Writing Data to infuxDB")
    client.write_points(json_body, database="iot-weather")
    time.sleep(60)
