from sqlalchemy import create_engine

from matplotlib import pyplot as plt

engine = create_engine('mysql://pi:squadleader@localhost/wormbin', echo = True)
cursor = engine.connect()
query = 'select * from Frank order by read_time DESC limit 10'
result = cursor.execute(query)
print("Records read successfully")
for row in result:
    print(row)

'''
x = [2,5,7]
y = [2,16,4]
plt.plot(x,y,label='my data')
plt.title('plus2net Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.grid(True,color='#f1f1f1')
plt.show()

'''
