import sqlite3
import time
import datetime

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import os.path

hfmt = matplotlib.dates.DateFormatter('%H:%M:%S')

#Initial database querry
conn = sqlite3.connect('wormbin.db')
c = conn.cursor()
wordUsed = 'read_time'
sql = "SELECT * FROM Frank ORDER BY read_time limit 80"


#plot run for wormtmp
graphArray = []
for row in c.execute(sql):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[1]+','+splitInfo[2]
    graphArray.append(graphArrayAppend)

read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})

fig = plt.figure()
rect = fig.patch
ax1 = fig.add_subplot(1,1,1, axisbg='white')
ax1.xaxis.set_major_formatter(hfmt)
wormtmp, = plt.plot_date(x=read_time, y=value, fmt='ro-', label = 'worm food temp', linewidth=2)

#Rerun for Tempf
graphArray = []
for row in c.execute(sql):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[1]+','+splitInfo[3]
    graphArray.append(graphArrayAppend)

read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})
tempf, =plt.plot_date(x=read_time, y=value, fmt='go-', label = 'Top of wormbin temp', linewidth=2)

#new sql query for outdoor temp
conn = sqlite3.connect('wormbin.db')
c = conn.cursor()
wordUsed = 'read_time'
sql = "SELECT * FROM Ester ORDER BY read_time limit 80"

#plot run for Ester outside
graphArray = []
for row in c.execute(sql):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[1]+','+splitInfo[3]
    graphArray.append(graphArrayAppend)

read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})
outside, =plt.plot_date(x=read_time, y=value, fmt='mD-', label = 'Outdoor temp', linewidth=2)

#new sql query for office floor temp
conn = sqlite3.connect('wormbin.db')
c = conn.cursor()
wordUsed = 'read_time'
sql = "SELECT * FROM Heidi ORDER BY read_time limit 80"

#plot run for Heidi inside
graphArray = []
for row in c.execute(sql):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[1]+','+splitInfo[3]
    graphArray.append(graphArrayAppend)

read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})
office, =plt.plot_date(x=read_time, y=value, fmt='b^-', label = 'Office floor corner temp', linewidth=2)




plt.xlabel('Time')
plt.ylabel('Temp F')
plt.title('Wormbin Activity Monitor\nWormtmp, Wormbin tmp, office tmp\noutside temperature')
plt.legend(bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure, ncol=1,fontsize = "small", shadow=True, title="Legend", fancybox=True)
plt.show()   
	  