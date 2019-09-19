# mbl-alpine-container

Alpine and Python container with I2C pass-through, thus allowing the sensors to be accessed from within the container.  Air Quality Sensor is working, GPS sensor is working, but Lightning Sensor is not.

A small script called "start.sh" in the root directory launches 'influxd' as a background process, then the index.py python application in the scripts directory.

We need to come up with a way to store the values, and ship them to the Ampere box.  Let's bypass the Edge nodes for now.  If you sync this repo, once it has downloaded, you need to move the "scripts" directory into the "rootfs" folder, and, check to see if the "start.sh" is executable...if not just chmod +x it.

 Then, run:
 
 opkg-build -Z "xz" -g root -o root . .

 tar -cvf alpine-python-iot.ipk.tar alpine-python-iot_1.0_any.ipk

 cp alpine-python-iot.ipk.tar ../update-resources/alpine-python-iot.ipk.tar

 cd ../update-resources/
 
 manifest-tool update device --device-id 016cee17a5260000000000010010022f --payload alpine-python-iot.ipk.tar --api-key ak_1MDE2OWY5ZjcxN2NhNWUwMjc0YzIxMDc3MDAwMDAwMDA016a0363d1145e0274c2107700000000Soxtd5TDuAYjzkiOC1HMibvaLq3oNGrz
 
 (change your device id accordingly...it can be found in Pelion web dashboard)
 
 It takes about 15 minutes to push the container, seemingly withought much progress, but it does work in the end.
 
 From an SSH session, you can run:

 runc exec alpine-python-iot sh  (to start a console inside the running container)
 
 influx -database 'iot-weather' -execute 'select * from fahrenheit' -pretty  (or other table as identified in the index.py fie)
