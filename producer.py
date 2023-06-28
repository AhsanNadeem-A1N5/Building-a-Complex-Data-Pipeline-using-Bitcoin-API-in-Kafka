import kafka
import time
import requests
import json
import websocket


url='https://api.coinbase.com/v2/prices/btc-pkr/buy'
url2='https://api.coinbase.com/v2/prices/btc-pkr/spot'
producer = kafka.KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda p:json.dumps(p).encode('ascii'))
while True:
    time.sleep(2)
    buy_price= (requests.get(url).json())
    spot_price= (requests.get(url2).json())
    print('Buy Price fetched and sent to Consumer',buy_price["data"]["amount"])
    print('Spot Price fetched and sent to Consumer',spot_price["data"]["amount"])
    buy_price=float(buy_price["data"]["amount"])
    spot_price=float(spot_price["data"]["amount"])
    prices=[buy_price,spot_price]
    producer.send('Profit_Loss',prices)
    
