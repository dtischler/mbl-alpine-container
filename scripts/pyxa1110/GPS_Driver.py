import smbus
import math
import time

class GPS:
    'Firstly this Driver was for SparkFun GPS Breakout - XA1110 (Qwiic) that uses I2C but this should work with other GPS devices with I2C, NMEA, PMTK'

    def __init__ (self, address = 0x10, bus_number = 1, debug = False):
        self.debug = debug
        self.address = address
        self.bus_number = bus_number
        self.data = [] 
        self.smbus = smbus.SMBus(bus_number)
        if self.debug:
            print("Conecting to 0x" + str(format(self.address, '02x')) + " on bus " + str(self.bus_number))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.smbus.close()
        if self.debug:
            print("Closing to 0x" + str(format(self.address, '02x')) + " on bus " + str(self.bus_number))

    def receiveData (self):
        """Receive data from GPS device"""
        self.data = []
        isEnd = False
        a = None
        b = None
        while True:
            if a is None and b is None:
                a = self.smbus.read_byte(self.address)
            elif a is not None and b is None:
                b = self.smbus.read_byte(self.address)
            elif a == 0x0D and b == 0x0A:
                break
            else:
                if a is not 0x0A:
                    self.data.append(a)
                a = b
                b = self.smbus.read_byte(self.address)


    def available (self):
        return bool(self.data)

    def ascii (self):
        """Returns received bytes decoded as ASCII"""
        return bytearray(self.data).decode('ascii')

    def bytes (self):
        return self.data

    def sendData (self, packet):
        if self.debug:
            print("Sending: " + packet)

        if len(packet) > 255:
            raise Exception("Command message to long")

        for c in bytearray(packet, 'ascii'):
            self.smbus.write_byte(self.address, c)

        time.sleep(0.02)

    def createMTKPacket (self, packetType, data):
        """
        Creates $PMTK packet

        Keyword arguments:
        packetType - number that indicates packet type
        data - extra data that will be send in packet
        """
        #default header
        configSequence = "$PMTK"

        #Attach leading zeros
        if packetType < 100: 
            configSequence += "0"
        if packetType < 10: 
            configSequence += "0"
        
        configSequence += str(packetType)

        if data:
            configSequence += data

        configSequence += "*" + self.getCRC(configSequence) + '\r' + '\n'
        return configSequence
    
    def getCRC (self, sequence):
        bytes = bytearray([0]) + bytearray(sequence[1:], 'ascii')

        for n in range(len(bytes)):
            bytes[0] ^= bytes[n]

        return format(bytes[0], '02x')