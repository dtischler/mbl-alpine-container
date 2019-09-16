#!/usr/bin/env python3

# -----------------------------------------------------------------------------
#                 Example Code for Qwiic Kit for Raspberry Pi
# -----------------------------------------------------------------------------
# Qwiic Starter Kit Demo for Raspberry Pi
# Read data from the BME280, CCS811, and VCNL4040 proximity sensor. Then display
# the data on the screen, the Micro OLED, and send MQTT data to Cayenne.
# By: Michelle Shorter @ SparkFun Electronics
# Original Creation Date: May 29, 2019
#
# For the hookup instructions and kit go to:
#      https://learn.sparkfun.com/tutorials/qwiic-kit-for-raspberry-pi-hookup-guide
#
# This code is beerware/beefware; if you see me (or any other SparkFun employee)
# at the local, and you've found our code helful, please buy us a beer/burger!
#
# Distributed as-is; no warranty is given
# -----------------------------------------------------------------------------

#Must download Qwiic Python Library - https://github.com/sparkfun/qwiic_py
from __future__ import print_function, division
import paho.mqtt.client as mqtt
import qwiic
import time
import sys

#These values are used to give BME280 and CCS811 some time to take samples
initialize=True
n=2

#MQTT Cayenne setup - you will need your own username, password and clientid
#To setup a Cayenne account go to https://mydevices.com/cayenne/signup/
username = "______ENTER_MQTT_USERNAME____"
password = "______ENTER_MQTT_PASSWORD____"
clientid = "___ENTER_CAYENNE_CLIENTE_ID___"
mqttc=mqtt.Client(client_id = clientid)
mqttc.username_pw_set(username, password = password)
mqttc.connect("mqtt.mydevices.com", port=1883, keepalive=60)
mqttc.loop_start()

#Qwiic Board define
prox = qwiic.QwiicProximity()
bme = qwiic.QwiicBme280()
ccs = qwiic.QwiicCcs811()
#oled = qwiic.QwiicMicroOled()

#Begin statements
prox.begin()
bme.begin()
#ccs.begin()
#oled.begin()

#Used for debugging CCS811
try:
    ccs.begin()

except Exception as e:
    print(e)

#Setup OLED
#oled.clear(oled.ALL)
#oled.display()
#oled.set_font_type(1)

#set MQTT topics (we are not setting topics for everything)
topic_bme_temp = "v1/" + username + "/things/" + clientid + "/data/1"
topic_bme_hum = "v1/" + username + "/things/" + clientid + "/data/2"
topic_bme_pressure = "v1/" + username + "/things/" + clientid + "/data/3"
topic_bme_altitude = "v1/" + username + "/things/" + clientid + "/data/4"

topic_prox_proximity = "v1/" + username + "/things/" + clientid + "/data/5"
topic_prox_ambient = "v1/" + username + "/things/" + clientid + "/data/6"

topic_ccs_temp = "v1/" + username + "/things/" + clientid + "/data/7"
topic_ccs_tvoc = "v1/" + username + "/things/" + clientid + "/data/8"
topic_ccs_co2 = "v1/" + username + "/things/" + clientid + "/data/9"

#Loop runs until we force an exit or something breaks
while True:
    try:
        if initialize==True:
            print ("Initializing: BME280 and CCS811 are taking samples before printing and publishing data!")
            print (" ")
        else:
            #print ("Finished initializing")
            n=1 #set n back to 1 to read sensor data once in loop
        for n in range (0,n):
            #print ("n = ", n) #used for debugging for loop

            #Proximity Sensor variables - these are the available read functions
            #There are additional functions not listed to set thresholds, current, and more
#            proximity = prox.get_proximity()
#            ambient = prox.get_ambient()
#            white = prox.get_white()
            #close = prox.is_close()
            #away = prox.is_away()
            #light = prox.is_light()
            #dark = prox.is_dark()
            #id = prox.get_id()

            #BME280 sensor variables
            #reference pressure is available to read or set for altitude calculation
            #referencePressure = bme.get_reference_pressure()
            #bme.set_reference_pressure(referencePressure)
            pressure = bme.get_reference_pressure() #in Pa
            altitudem = bme.get_altitude_meters()
            altitudef = bme.get_altitude_feet()
            humidity = bme.read_humidity()
            tempc = bme.get_temperature_celsius()
            tempf = bme.get_temperature_fahrenheit()
            dewc = bme.get_dewpoint_celsius()
            dewf = bme.get_dewpoint_fahrenheit()

            #CCS811 sensor variables
            #ccsbaseline = get_baseline() #used for telling sensor what 'clean' air is
            #set_baseline(ccsbaseline)
            #error = ccs.check_status_error()
            #data = ccs.data_available()
            #app = ccs.app_valid()
            #errorRegister = ccs.get_error_register()
            #ccs.enable_interrupts()
            #ccs.disable_interrupts()
            #ccs.set_drive_mode(mode) #Mode0=Idle, Mode1=read every 1s, Mode2=read every 10s, Mode3=read every 60s, Mode4=RAW mode
            #ccs.set_environmental_data(humidity,temperature)

            ccs.read_algorithm_results() #updates the TVOC and CO2 values
            tvoc = ccs.get_tvoc()
            co2 = ccs.get_co2()

            #Note:The following values are used when is a NTC thermistor attached to the CCS811 breakout board
            #the environmental combo does not breakout the pins like the breakout board
            #ccs.set_reference_resistance()
            #ccs.read_ntc() #updates temp value
            #ccstemp = ccs.get_temperature()
            #ccsres = ccs.get_resistance()

            #Give some time for the BME280 and CCS811 to initialize when starting up
            if initialize==True:
                time.sleep(10)
                initialize=False

        #printing time and some variables to the screen
        #https://docs.python.org/3/library/time.html
        #print (time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())) #24-hour time
        print (time.strftime("%a %b %d %Y %I:%M:%S%p", time.localtime())) #12-hour time

        print ("BME Temperature %.1f F" %tempf)
        print ("Humidity %.1f" %humidity)

        print ("Pressure %.2f Pa" %pressure)
        print ("Altitude %.2f ft" %altitudef)

        #print ("CCS Temperature %.1f F" %ccstemp)
#        print ("Distance %.2f " %proximity)
#        print ("Ambient Light %.2f" %ambient)

        print ("TVOC %.2f" %tvoc)
        print ("CO2 %.2f" %co2)

        print (" ") #blank line for easier readability

        #publishing data to Cayenne (we are not publishing everything)
        mqttc.publish (topic_bme_temp, payload = tempf, retain = True)
        mqttc.publish (topic_bme_hum, payload = humidity, retain = True)
        mqttc.publish (topic_bme_pressure, payload = pressure, retain = True)
        mqttc.publish (topic_bme_altitude, payload = altitudef, retain = True)

#        mqttc.publish (topic_prox_proximity, payload = proximity, retain = True)
#        mqttc.publish (topic_prox_ambient, payload = ambient, retain = True)

        #mqttc.publish (topic_ccs_temp, payload = ccstemp, retain = True)
        mqttc.publish (topic_ccs_tvoc, payload = tvoc, retain = True)
        mqttc.publish (topic_ccs_co2, payload = co2, retain = True)

        #displaying data to the OLED (we are only displaying a few things because of screen size)
        #with font1 a y difference of 16 is good spacing for each line
        #we are converting values to int before printing for space (and we don't really need better resolution)
#        oled.clear(oled.PAGE)

#        oled.set_cursor(0,0)
#        oled.print("Tmp:")
#        oled.print(int(tempf))
#        oled.print("F")
        #oled.print(int(temc))
        #oled.print("C")

#        oled.set_cursor(0,16)
#        oled.print("RH%:") #Relative Humidity
#        oled.print(int(humidity))
#        oled.set_cursor(0,32)
#        oled.print("hPa:") #hPa is a more typical output and helps with spacing
#        oled.print(int(pressure/100))

#        oled.display()

        #delay (number of seconds) so we are not constantly displaying data and overwhelming devices
        time.sleep(60)


    #if we break things or exit then exit cleanly
    except (EOFError, SystemExit, KeyboardInterrupt):
        mqttc.disconnect()
        sys.exit()
