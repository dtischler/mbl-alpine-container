import pynmea2
import pyxa1110

def getGNGGA():
  gngga = ''
  with pyxa1110.GPS(debug = True) as gps:
    for n in range(10):
      gps.receiveData()
      data = gps.ascii()
      if data.startswith("$GNGGA"):
        gngga = data
  return gngga

def getCoordinates():
  raw = getGNGGA()
  parsed = pynmea2.parse(raw)
  return (parsed.latitude, parsed.longitude)
