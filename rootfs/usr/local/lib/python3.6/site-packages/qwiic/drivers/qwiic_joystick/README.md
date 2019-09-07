Qwiic_Joystick_Py
==================

<p align="center">
   <img src="https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo-registered.jpg"  width=200>  
   <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"  width=240>   
</p>
<p align="center">
	<a href="https://pypi.org/project/sparkfun-qwiic-joystick/" alt="Package">
		<img src="https://img.shields.io/pypi/pyversions/sparkfun_qwiic_joystick.svg" /></a>
	<a href="https://github.com/sparkfun/Qwiic_Joystick_Py/issues" alt="Issues">
		<img src="https://img.shields.io/github/issues/sparkfun/Qwiic_Joystick_Py.svg" /></a>
	<a href="https://qwiic-joystick-py.readthedocs.io/en/latest/?" alt="Documentation">
		<img src="https://readthedocs.org/projects/qwiic-joystick-py/badge/?version=latest&style=flat" /></a>
	<a href="https://github.com/sparkfun/Qwiic_Joystick_Py/blob/master/LICENSE" alt="License">
		<img src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>
	<a href="https://twitter.com/intent/follow?screen_name=sparkfun">
        	<img src="https://img.shields.io/twitter/follow/sparkfun.svg?style=social&logo=twitter"
           	 alt="follow on Twitter"></a>
	
</p>

<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg"  align="right" width=300 alt="SparkFun Qwiic Joystick Breakout">

Python module for the qwiic joystick, which is part of the [SparkFun Qwiic Joystick](https://www.sparkfun.com/products/15168)

This python package is a port of the existing [SparkFun Qwiic Joystick Arduino Library](https://github.com/sparkfun/SparkFun_Qwiic_Joystick_Arduino_Library)

This package can be used in conjunction with the overall [SparkFun qwiic Python Package](https://github.com/sparkfun/Qwiic_Py)

New to qwiic? Take a look at the entire [SparkFun qwiic ecosystem](https://www.sparkfun.com/qwiic).

## Contents

* [Dependencies](#dependencies)
* [Installation](#installation)
* [Documentation](#documentation)
* [Example Use](#example-use)

Dependencies 
---------------
This driver package depends on the qwiic I2C driver: 
[Qwiic_I2C_Py](https://github.com/sparkfun/Qwiic_I2C_Py)

Documentation
-------------
The SparkFun qwiic Joystick module documentation is hosted at [ReadTheDocs](https://qwiic-joystick-py.readthedocs.io/en/latest/?)

Installation
-------------

### PyPi Installation
This repository is hosted on PyPi as the [sparkfun-qwiic-joystick](https://pypi.org/project/sparkfun-qwiic-joystick/) package. On systems that support PyPi installation via pip, this library is installed using the following commands

For all users (note: the user must have sudo privileges):
```sh
sudo pip install sparkfun-qwiic-joystick
```
For the current user:

```sh
pip install sparkfun-qwiic-joystick
```

### Local Installation
To install, make sure the setuptools package is installed on the system.

Direct installation at the command line:
```sh
python setup.py install
```

To build a package for use with pip:
```sh
python setup.py sdist
 ```
A package file is built and placed in a subdirectory called dist. This package file can be installed using pip.
```sh
cd dist
pip install sparkfun_qwiic_joystick-<version>.tar.gz
  
```
Example Use
 ---------------
See the examples directory for more detailed use examples.

```python
from __future__ import print_function
import qwiic_joystick
import time
import sys

def runExample():

	print("\nSparkFun qwiic Joystick   Example 1\n")
	myJoystick = qwiic_joystick.QwiicJoystick()

	if myJoystick.isConnected() == False:
		print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	myJoystick.begin()

	print("Initialized. Firmware Version: %s" % myJoystick.getVersion())

	while True:

		print("X: %d, Y: %d, Button: %d" % ( \
					myJoystick.getHorizontal(), \
					myJoystick.getVertical(), \
					myJoystick.getButton()))

		time.sleep(.5)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 1")
		sys.exit(0)

```
<p align="center">
<a href="https://www.sparkfun.com" alt="SparkFun">
<img src="https://cdn.sparkfun.com/assets/custom_pages/3/3/4/dark-logo-red-flame.png" alt="SparkFun - Start Something"></a>
</p>
