Qwiic_Twist_Py
==================

<p align="center">
   <img src="https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo-registered.jpg"  width=200>  
   <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"  width=240>   
</p>
<p align="center">
	<a href="https://pypi.org/project/sparkfun-qwiic-twist/" alt="Package">
		<img src="https://img.shields.io/pypi/pyversions/sparkfun_qwiic_twist.svg" /></a>
	<a href="https://github.com/sparkfun/Qwiic_Twist_Py/issues" alt="Issues">
		<img src="https://img.shields.io/github/issues/sparkfun/Qwiic_Twist_Py.svg" /></a>
	<a href="https://qwiic-twist-py.readthedocs.io/en/latest/?" alt="Documentation">
		<img src="https://readthedocs.org/projects/qwiic-twist-py/badge/?version=latest&style=flat" /></a>
	<a href="https://github.com/sparkfun/Qwiic_Twist_Py/blob/master/LICENSE" alt="License">
		<img src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>
	<a href="https://twitter.com/intent/follow?screen_name=sparkfun">
        	<img src="https://img.shields.io/twitter/follow/sparkfun.svg?style=social&logo=twitter"
           	 alt="follow on Twitter"></a>
	
</p>

<img src="https://cdn.sparkfun.com//assets/parts/1/3/4/3/3/15083-SparkFun_Qwiic_Twist_-_RGB_Rotary_Encoder_Breakout-01.jpg"  align="right" width=300 alt="SparkFun Qwiic Twist Breakout">

Python module for the qwiic twist, which is part of the [SparkFun Qwiic Twist](https://www.sparkfun.com/products/15083)

This python package is a port of the existing [SparkFun Qwiic Twist Arduino Library](https://github.com/sparkfun/SparkFun_Qwiic_Twist_Arduino_Library)

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
The SparkFun qwiic Twist module documentation is hosted at [ReadTheDocs](https://qwiic-twist-py.readthedocs.io/en/latest/?)

Installation
-------------

### PyPi Installation
This repository is hosted on PyPi as the [sparkfun-qwiic-twist](https://pypi.org/project/sparkfun-qwiic-twist/) package. On systems that support PyPi installation via pip, this library is installed using the following commands

For all users (note: the user must have sudo privileges):
```sh
sudo pip install sparkfun-qwiic-twist
```
For the current user:

```sh
pip install sparkfun-qwiic-twist
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
pip install sparkfun_qwiic_twist-<version>.tar.gz
  
```
Example Use
 ---------------
See the examples directory for more detailed use examples.

```python
import qwiic_twist
import time
import sys

def runExample():

	print("\nSparkFun qwiic Twist   Example 1\n")
	myTwist = qwiic_twist.QwiicTwist()

	if myTwist.connected == False:
		print("The Qwiic twist device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	myTwist.begin()

	# Set the knob color to pink
	myTwist.set_color(100, 10, 50)

	while True:

		print("Count: %d, Pressed: %s" % (myTwist.count, \
			"YES" if myTwist.pressed else "NO", \
			))

		time.sleep(.3)

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
