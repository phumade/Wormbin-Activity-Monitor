##!/usr/bin/python3
import time
import datetime
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.dates
import matplotlib.dates as mdates

import os
import sys



hfmt = matplotlib.dates.DateFormatter('%H:%M:%S')

#Reading from to local sql server
engine = create_engine('mysql://pi:squadleader@192.168.1.5/wormbin', echo = False)
Session = sessionmaker(bind=engine)
session = Session()
print ("Reading from table...")
#Initial database querry

cursor = engine.connect()
sql = "SELECT * FROM wormbin.Frank union select * from wormbin.Heidi ORDER BY read_time DESC LIMIT 10"
cursor.execute(sql)
result = cursor.fetchall()
print(result)

#plot run for frank
wordUsed = 'read_time'
graphArray = []
for row in result:
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[1]+','+splitInfo[5]
    graphArray.append(graphArrayAppend)

read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                               converters={ 0: mdates.strpdate2num(' %Y-%m-%d %H:%M:%S')})

fig = plt.figure()
rect = fig.patch
ax1 = fig.add_subplot(1,1,1)
ax1.xaxis.set_major_formatter(hfmt)
wormtmp, = plt.plot_date(x=read_time, y=value, fmt='ro-', markersize = 3, label = 'Wormbin Barometric Pressure', linewidth=2)

#new sql query for Ester outdoor temp
wordUsed = 'read_time'
sql = "SELECT * FROM Ester ORDER BY read_time limit 1440"
cursor.execute(sql)
result = cursor.fetchall()
#plot run for Ester outside
graphArray = []
for row in result:
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[1]+','+splitInfo[5]
    graphArray.append(graphArrayAppend)

read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                               converters={ 0: mdates.strpdate2num(' %Y-%m-%d %H:%M:%S')})
outside, =plt.plot_date(x=read_time, y=value, fmt='mD-', markersize = 3, label = 'Outdoor Barometric Pressure', linewidth=2)

#new sql query for office floor temp
wordUsed = 'read_time'
sql = "SELECT * FROM Heidi ORDER BY read_time limit 1440"
cursor.execute(sql)
result = cursor.fetchall()
#plot run for Heidi inside
graphArray = []
for row in result:
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[1]+','+splitInfo[5]
    graphArray.append(graphArrayAppend)

read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                               converters={ 0: mdates.strpdate2num(' %Y-%m-%d %H:%M:%S')})
office, =plt.plot_date(x=read_time, y=value, fmt='b^-', markersize = 3, label = 'Office floor corner Barometric Pressure', linewidth=2)




plt.xlabel('Time of Day')
plt.ylabel('Barometric Pressure mBar')
plt.title('W.A.M Barometric Pressuure\n Wormbin, Office, Outside')
plt.legend(bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure, ncol=1,fontsize = "small", shadow=True, title="Legend", fancybox=True)

#print "Current working dir : %s" % os.getcwd()
#print(os.listdir('.'))
plt.show()
#print(os.path.abspath(appworms.py))
#plt.savefig('/home/pi/worms/static/ba_pressure.png')
print("success")

