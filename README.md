# mbl-alpine-container

Alpine and Python container with I2C pass-through, thus allowing the sensors to be accessed from within the container.  Air Quality Sensor is working, GPS sensor is working, but Lightning Sensor is not.

A small script called "start.sh" in the root directory launches 'influxd' as a background process, then the index.py python application in the 'scripts' directory.

The working theory is that the IoT Endpoints collect the data via the sensors, and send MQTT data to the Edge Nodes.  The Edge Nodes then use "mqttwarn" to take the JSON, convert to influx, and publish to the Cloud Server.  If you sync this repo, once it has downloaded, you need to move the "scripts" directory into the "rootfs" folder, and, check to see if the "start.sh" is executable...if not just chmod +x it.

 Once it is cloned to your Yoga and the 'scripts' directory moved down a level, run:
 
 opkg-build -Z "xz" -g root -o root . .

 tar -cvf alpine-python-iot.ipk.tar alpine-python-iot_1.0_any.ipk

 cp alpine-python-iot.ipk.tar ../update-resources/alpine-python-iot.ipk.tar

 cd ../update-resources/
 
 manifest-tool update device --device-id xxxxxxx --payload alpine-python-iot.ipk.tar --api-key ak_xxxxxxx
 
 (change your device id accordingly...it can be found in Pelion web dashboard)
 
 It takes about 15 minutes to push the container.
 
 If you then launch an SSH session, you can run:

 runc exec alpine-python-iot sh  (to start a console inside the running container)
 
 influx -database 'iot-weather' -execute 'select * from fahrenheit' -pretty  (or other table as identified in the index.py file)
