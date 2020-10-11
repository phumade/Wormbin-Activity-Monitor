import io
import os
import random
import json
from flask_mysqldb import MySQL
from flask import Flask, render_template, request, url_for, Response, make_response


from dateutil import parser

app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'pi'
app.config['MYSQL_PASSWORD'] = 'squadleader'
app.config['MYSQL_DB'] = 'wormbin'

mysql = MySQL(app)

@app.route("/")
def main():
   # connects to SQLite database. File is named "wormbin.db" without the quotes
   # WARNING: your database file should be in the same directory of the appworms.py file or have the correct path
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM wormbin.Frank union select * from wormbin.Heidi ORDER BY read_time DESC LIMIT 10")
   readings = cur.fetchall()
   cur.close()
#   print(readings)
   return render_template('start.html', readings=readings)

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
   app.run(host='192.168.1.05')
