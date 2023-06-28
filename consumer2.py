from kafka import KafkaConsumer
import pymongo
import json

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["Commission"]
mycol=mydb["CommValue"]
consumer=KafkaConsumer('Commission',bootstrap_servers=['localhost:9092'])
commission_rate=0.5
for message in consumer:
	values=message.value.decode('ascii')
	values=values.split(',')
	#values=list(values)
	v1=float(values[0][1:])
	v2=float(values[1][:len(values[1])-1])
	transaction_value=abs(v2-v1)
	commission=(transaction_value*commission_rate)/100
	x={"Buy":v1,"Sell":v2,"CommValue":commission}
	#data=json.loads(x)
	mycol.insert_one(x)
	print("Commission is: ",x)
