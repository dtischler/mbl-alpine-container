# mbl-alpine-container

Alpine and Python container with I2C pass-through, thus allowing the sensors to be accessed from within the container.  Air Quality Sensor is working, GPS sensor is working, but Lightning Sensor is not.


TODO:  The python fles in the rootfs folder are proof of concept, and read data, but do not do anything with it.  
Only air.py and gps.py work, but lightning.py does not.


gps.py returns back the NMEA coordinates, though they still need to be parsed and converted to Lat/Long.  There seem to be some utilities for that.

air.py is a loop that returns the current Temp, Pressure, TVOC, and CO2 every 20 seconds.

lightning.py gives an error.


config.json can be modified to run any of the python scripts that you prefer upon launching the container, by changling line 10 from:

"sh"

to:

"python3",
"air.py"


(It needs to be on two lines like that example)

In any case, we need to come up with a way to store the values, and ship them to the Ampere box.  Let's bypass the Edge nodes for now.

 After cloning, run:
 
 opkg-build -Z "xz" -g root -o root . .
 tar -cvf alpine-python-iot.ipk.tar alpine-python-iot_1.0_any.ipk
 cp alpine-python-iot.ipk.tar ../update-resources/alpine-python-iot.ipk.tar
 cd ../update-resources/
 mbl-cli -a 192.168.0.xxx put alpine-python-iot.ipk.tar /scratch
 mbl-cli -a 192.168.0.xxx shell
 
 
 Now on the node:
 
 runc help (because the commands are different than Docker)
 runc list (to see if the container is running)
 runc exec alpine-python sh (to poke around in the container)
 
