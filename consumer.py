from kafka import KafkaConsumer
import pymongo
import json

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["Profit-Loss"]
mycol=mydb["P/L Value"]
consumer=KafkaConsumer('Profit_Loss',bootstrap_servers=['localhost:9092'])
for message in consumer:
	values=message.value.decode('ascii')
	values=values.split(',')
	#values=list(values)
	v1=float(values[0][1:])
	v2=float(values[1][:len(values[1])-1])
	val=v2-v1
	status=""
	if val<0:
		status="Loss"
	else:
		status="Profit"
	x={"Status":status,"Value":val}
	#data=json.loads(x)
	mycol.insert_one(x)
	print("Profit/Loss is: ",x)
