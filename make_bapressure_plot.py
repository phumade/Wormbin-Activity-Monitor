import sqlite3
import mysql.connector
import time
import datetime

import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


hfmt = matplotlib.dates.DateFormatter('%H:%M:%S')
#Initial database querry
conn = sqlite3.connect('wormbin.db')
c = conn.cursor()

sql = "SELECT * FROM Frank ORDER BY read_time limit 1440"


graphArray = []
for row in c.execute(sql):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[1]+','+splitInfo[2]
    graphArray.append(graphArrayAppend)

datestamp, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={ 0: mdates.strpdate2num(' %Y-%m-%d %H:%M:%S')})

fig = plt.figure()

rect = fig.patch

ax1 = fig.add_subplot(1,1,1, axisbg='white')
plt.plot_date(x=datestamp, y=value, fmt='b-', label = 'value', linewidth=2)
plt.show()   