from time import gmtime, localtime, strftime
import time
import datetime
import paho.mqtt.client as mqtt
import sqlite3

wormtmp = "wormtmp"
temperature_topic = "tempf"
humidity_topic = "humidity"
ba_pressure = "ba_pressure"
dbFile = "wormbin.db"

dataTuple = [-1,-1,-1,-1]

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to mqtt with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Genie/#")
    client.subscribe("Frank/#")
    client.subscribe("Carla/#")
    client.subscribe("Heidi/#")
    client.subscribe("Ester/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    theTime = strftime("%Y-%m-%d %H:%M:%S", localtime())
    result = (theTime + "\t" + str(msg.payload))
    print(msg.topic + ":\t\t" + result)
 #   print(msg.topic[6:])
    collector=msg.topic[0:5]
    if (msg.topic[6:] == wormtmp):
        dataTuple[0] = str(msg.payload)
    if (msg.topic[6:] == temperature_topic):
        dataTuple[1] = str(msg.payload)
    if (msg.topic[6:] == humidity_topic):
        dataTuple[2] = str(msg.payload)
    if (msg.topic[6:] == ba_pressure):
        dataTuple[3] = str(msg.payload)
        #return
    if (collector != 'Frank'):
        dataTuple[0] = str(0)    
    if (dataTuple[0] !=-1 and dataTuple[1] != -1 and dataTuple[2] != -1 and dataTuple[3] != -1):
        writeToDb(collector, theTime, dataTuple[0], dataTuple[1], dataTuple[2], dataTuple[3])
    return


def writeToDb(collector, theTime, wormtmp, tempf, humidity, ba_pressure):
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    print ("Writing to %s table..." % (collector))
#    sqlite_insert_query ="INSERT INTO wormbin (read_time, wormtmp, tempf, humidity, ba_pressure) VALUES (?,?,?,?,?)", (theTime, wormtmp, tempf, humidity, ba_pressure)
#    c.execute(sqlite_insert_query)
    c.execute("INSERT INTO %s (read_time, wormtmp, tempf, humidity, ba_pressure, name) VALUES (?,?,?,?,?,?)" % (collector), (theTime, wormtmp, tempf, humidity, ba_pressure, collector))
    conn.commit()
    global dataTuple
    dataTuple = [-1,-1,-1,-1]
    print ("Success! A measurement was written to %s\n" % (collector))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.20", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
