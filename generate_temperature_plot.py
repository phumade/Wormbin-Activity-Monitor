import sqlite3
import time
import datetime

import numpy as np
import matplotlib
#if matplot commented then display local
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import os

hfmt = matplotlib.dates.DateFormatter('%H:%M:%S')
#Initial database querry
conn = sqlite3.connect('wormbin.db')
c = conn.cursor()
wordUsed = 'read_time'
sql = "SELECT * FROM Frank ORDER BY read_time limit 1440"


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
wormtmp, = plt.plot_date(x=read_time, y=value, fmt='ro-', markersize=2, label = 'worm food temp', linewidth=2)

#Rerun for Tempf
graphArray = []
for row in c.execute(sql):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[1]+','+splitInfo[3]
    graphArray.append(graphArrayAppend)

read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})
tempf, =plt.plot_date(x=read_time, y=value, fmt='go-', markersize=2, label = 'Top of wormbin temp', linewidth=2)

#new sql query for outdoor temp
conn = sqlite3.connect('wormbin.db')
c = conn.cursor()
wordUsed = 'read_time'
sql = "SELECT * FROM Ester ORDER BY read_time limit 1440"

#plot run for Ester outside
graphArray = []
for row in c.execute(sql):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[1]+','+splitInfo[3]
    graphArray.append(graphArrayAppend)

read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})
outside, =plt.plot_date(x=read_time, y=value, fmt='mD-', markersize=2, label = 'Outdoor temp', linewidth=2)

#new sql query for office floor temp
conn = sqlite3.connect('wormbin.db')
c = conn.cursor()
wordUsed = 'read_time'
sql = "SELECT * FROM Heidi ORDER BY read_time limit 1440"

#plot run for Heidi inside
graphArray = []
for row in c.execute(sql):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[1]+','+splitInfo[3]
    graphArray.append(graphArrayAppend)

read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})
office, =plt.plot_date(x=read_time, y=value, markersize=2, fmt='b^-', label = 'Office floor corner temp', linewidth=2)




plt.xlabel('Time of Day')
plt.ylabel('Temp F')
plt.title('W.A.M Temp F\nWormtmp, Wormbin tmp, Office tmp\noutside temperature')
plt.legend(bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure, ncol=1,fontsize = "small", shadow=True, title="Legend", fancybox=True)

#print "Current working dir : %s" % os.getcwd()
#print(os.listdir('.'))
plt.show()
#plt.savefig('/Volumes/Rpi4www/flask/worms/static/tempf.png')
