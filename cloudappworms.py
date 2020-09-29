import io
import os
import random
import json
from flask_mysqldb import MySQL
from flask import Flask, render_template, request, url_for, Response, make_response, jsonify
from db import get_Frank, get_Heidi, get_Ester

from dateutil import parser

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'squadleader'
app.config['MYSQL_DB'] = 'wormbin'

mysql = MySQL(app)

@app.route("/", methods=['POST', 'GET')
def songs():
    return get_Frank()  


#def main():

   # connects to SQLite database. File is named "wormbin.db" without the quotes
   # WARNING: your database file should be in the same directory of the appworms.py file or have the correct path
#   cur = mysql.connection.cursor()
#   cur.execute("SELECT * FROM wormbin.Frank ORDER BY read_time DESC LIMIT 1440")
#   readings = cur.fetchall()
#   mysql.connection.commit()
#   cur.close()
#   print(readings)
#   return render_template('start.html', readings=readings)

@app.route("/Frank")
def Frank():
   # connects to SQLite database. File is named "sensordata.db" without the quotes
   # WARNING: your database file should be in the same directory of the appworms.py file or have the correct path
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM Frank ORDER BY read_time DESC LIMIT 1440")
   readings = cur.fetchall()
   #print(readings)
   return render_template('main.html', readings=readings, location = 'Frank')

@app.route("/Heidi")
def Heidi():
   # connects to SQLite database. File is named "sensordata.db" without the quotes
   # WARNING: your database file should be in the same directory of the appworms.py file or have the correct path
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM Heidi ORDER BY read_time DESC LIMIT 1440")
   readings = cur.fetchall()
   #print(readings)
   return render_template('main.html', readings=readings, location = 'Heidi')

@app.route("/Ester")
def Ester():
   # connects to SQLite database. File is named "sensordata.db" without the quotes
   # WARNING: your database file should be in the same directory of the app.py file or have the correct path
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM Ester ORDER BY read_time DESC LIMIT 1440")
   readings = cur.fetchall()
   #print(readings)
   return render_template('main.html', readings=readings, location = 'Ester')

@app.route("/Carla")
def Carla():
   # connects to SQLite database. File is named "sensordata.db" without the quotes
   # WARNING: your database file should be in the same directory of the app.py file or have the correct path
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM Carla ORDER BY read_time DESC LIMIT 1440")
   readings = cur.fetchall()
   #print(readings)
   return render_template('main.html', readings=readings, location = 'Carla')

@app.route("/Genie")
def Genie():
   # connects to SQLite database. File is named "sensordata.db" without the quotes
   # WARNING: your database file should be in the same directory of the app.py file or have the correct path
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM Genie ORDER BY read_time DESC LIMIT 1440")
   readings = cur.fetchall()
   #print(readings)
   return render_template('main.html', readings=readings, location = 'Genie')

@app.route("/plot")
def plot():
   os.system('python generate_ba_pressure_plot.py')
   os.system('python generate_humidity_plot()')
   os.system('python generate_temperature_plot.py')

   return render_template('start.html')


if __name__ == "__main__":
   app.run()
