import pyxa1110

#This code gets NMEA frames one by one
with pyxa1110.GPS(debug = True) as gps:
    for n in range(10):
        gps.receiveData()
        print(gps.ascii())
