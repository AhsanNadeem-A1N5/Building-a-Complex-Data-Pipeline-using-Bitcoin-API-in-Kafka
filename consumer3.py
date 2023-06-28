from kafka import KafkaConsumer
import pymongo
import json

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["MarkupPct"]
mycol=mydb["MkPctValue"]
consumer=KafkaConsumer('MarkupPercentage',bootstrap_servers=['localhost:9092'])

for message in consumer:
	values=message.value.decode('ascii')
	values=values.split(',')
	#values=list(values)
	v1=float(values[0][1:])
	v2=float(values[1][:len(values[1])-1])
	MarkupPct=((v2-v1)/v1)*100
	x={"Buy":v1,"Sell":v2,"MarkUpVal":MarkupPct}
	#data=json.loads(x)
	mycol.insert_one(x)
	print("Markup Percentage is: ",x)
    
