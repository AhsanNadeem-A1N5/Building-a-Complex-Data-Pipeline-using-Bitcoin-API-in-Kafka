import kafka
import time
import requests
import json
import websocket


url='https://api.coinbase.com/v2/prices/btc-pkr/buy'
url2='https://api.coinbase.com/v2/prices/btc-pkr/sell'
producer = kafka.KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda p:json.dumps(p).encode('ascii'))
while True:
    time.sleep(2)
    buy_price= (requests.get(url).json())
    sell_price= (requests.get(url2).json())
    print('Buy Price fetched and sent to Consumer',buy_price["data"]["amount"])
    print('Sell Price fetched and sent to Consumer',sell_price["data"]["amount"])
    buy_price=float(buy_price["data"]["amount"])
    sell_price=float(sell_price["data"]["amount"])
    prices=[buy_price,sell_price]
    producer.send('MarkupPercentage',prices)
    
