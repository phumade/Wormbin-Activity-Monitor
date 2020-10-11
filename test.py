import datetime
import os
import sys

from sqlalchemy import create_engine
#Make sure sqlalchemy works


#engine = create_engine('sqlite:///wormbin.db', echo = True)
engine = create_engine('mysql://pi:squadleader@localhost/wormbin', echo = True)
cursor = engine.connect()
query = 'select * from Frank order by read_time DESC limit 10'
result = cursor.execute(query)
print("Records read successfully")
for row in result:
    print(row)
