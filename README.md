# Wormbin Application Monitor
This project is an attempt to learn modern web technolgies and apply those tools to creat a wormbin monitoring tool.

There are 3 phases to this project.

1.  Develop a physical microcontroller package that includes various environmental sensors.
The main sensor package is comprised of a microcontroller (ESP8266) managing sensors using the i2c protocol. The main benefit of pairing the ESP8266 with i2c sensors is low cost, excellent documentation and wide commercial availability. Microcontroller code was written in C and various sensor libraries depend heavily on open source software. All Arduino sketches are available by private inquiry.
The main mensors are esp8266 controllers paired with BMP269 Temp/humidity/ba pressure sensor.  I used a DS18B20 digital temperature probe to direct readings from the wormpile.

2.  Develp a Flask web application
	a. Static Website application: check
	b. database logging Temp, Humidity, Ba Pressure: Check
	c.Python Intergration to Database: Check
	d. Flask Integration to Database: Check
	e. Static HTML, dynamic python, styling all look correct through Nginx
	f. SQL database: check


3.  Deploy that flask web application onto the public internet via Google compute/ Amazon AWS, or microsoft Azure.
	a.Goggle Cloud Computre or AWS: check
	b.Cloud Storage: Open
	c, Application Engine: Open
	d.Database: Open


