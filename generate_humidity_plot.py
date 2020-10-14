import sqlite3
import time
import datetime

import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates
import matplotlib.dates as mdates

import os

hfmt = matplotlib.dates.DateFormatter('%H:%M:%S')

#Initial database querry
conn = sqlite3.connect('wormbin.db')
c = conn.cursor()
wordUsed = 'read_time'
sql = "SELECT * FROM Frank ORDER BY read_time limit 1440"

def bytespdate2num(b):
    return mdates.datestr2num(b.decode('utf-8'))

#plot run for frank
graphArray = []
for row in c.execute(sql):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[1]+','+splitInfo[4]
    graphArray.append(graphArrayAppend)
'''
read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={ 0: mdates.strpdate2num(' %Y-%m-%d %H:%M:%S')})
'''
read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={ 0: bytespdate2num})

fig = plt.figure()
rect = fig.patch
ax1 = fig.add_subplot(1,1,1, axisbg='white')
ax1.xaxis.set_major_formatter(hfmt)
wormtmp, = plt.plot_date(x=read_time, y=value, fmt='ro-', markersize=2, label = 'Wormbin Humidity', linewidth=2)

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
    graphArrayAppend = splitInfo[1]+','+splitInfo[4]
    graphArray.append(graphArrayAppend)

read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={ 0: mdates.strpdate2num(' %Y-%m-%d %H:%M:%S')})
outside, =plt.plot_date(x=read_time, y=value, fmt='mD-', markersize=2, label = 'Outdoor Humidity', linewidth=2)

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
    graphArrayAppend = splitInfo[1]+','+splitInfo[4]
    graphArray.append(graphArrayAppend)

read_time, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={ 0: mdates.strpdate2num(' %Y-%m-%d %H:%M:%S')})
office, =plt.plot_date(x=read_time, y=value, fmt='b^-', markersize=2, label = 'Office floor corner Humidity', linewidth=2)




plt.xlabel('Time of day')
plt.ylabel('Humidity %')
plt.title('W.A.M Humidity\n Wormbin Humity, office Humidity\nOutside Humidity')
plt.legend(bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure, ncol=1,fontsize = "small", shadow=True, title="Legend", fancybox=True)


#print "Current working dir : %s" % os.getcwd()
#print(os.listdir('.'))
plt.show()
plt.savefig('/Volumes/Rpi4www/flask/worms/static/humidity.png')