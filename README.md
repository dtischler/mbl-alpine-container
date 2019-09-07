# mbl-alpine-container

TODO:  The python fles in the rootfs folder are not complete.  Only air.py and gps.py work, but lightning.py does not.


gps.py returns back the NMEA coordinates, though they still need to be parsed and converted to Lat/Long.
air.py is a loop that returns the current Temp, Pressure, TVOC, and CO2.
lightning.py gives an error.


config.json can be modified to run any of the python scripts that you prefer.


In any case, we need to come up with a way to store the values, and ship them to the Ampere box.  Let's bypass the Edge nodes for now.

 After cloning, run:
 
 opkg-build -Z "xz" -g root -o root . .
 tar -cvf alpine-python-iot.ipk.tar alpine-python-iot_1.0_any.ipk
 cp alpine-python-iot.ipk.tar ../update-resources/alpine-python-iot.ipk.tar
 cd ../update-resources/
 mbl-cli -a 192.168.0.xxx put alpine-python-iot.ipk.tar /scratch
 mbl-cli -a 192.168.0.xxx shell
 
 
 Now on the node:
 
 runc list
