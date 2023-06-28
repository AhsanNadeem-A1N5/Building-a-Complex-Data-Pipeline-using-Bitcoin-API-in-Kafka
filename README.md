
##Stock Data Kafka Implementation

System Requirements:
1. Kafka Installed and configured.
2. MongoDb configured on PC.
3. Place 'producer.py','consumer.py','producer2.py','consumer2.py',consumer3.py','producer3.py' in the bin folder of your Kafka.


## Run the Stocks Info

1. Open a terminal and type following command to start MongoDb;

```bash
  mongosh
```

2. Go to 'bin' folder in your Kafka folder, then open a Second Terminal and create a Kafka topic named "Profit-Loss" with replication factor 1 :
```bash
    cd kafka
```
```bash
    cd bin
```

```bash
    ./kafka-topics.sh --create --topic Profit-Loss --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```
3. On the same terminal run the following producer:
```bash
    python3 producer.py
```
4. Now open a Third Terminal (keeping open the the other two in the background) and type:
```bash
    python3 consumer.py
```
5. Now you will see the data being sent from the producer to consumer, the calculations on data are being done in consumer and showing on the terminal as well as storing in MongoDb database, you can check the database automatically made in the MongoDb terminal(First One) by typing:
```bash
    show  dbs
```
6. Now first its is the turn of Second producer and Second consumer, close the producer and consumer terminals and open new ones and repeat step 2 onwards but creating different topic this time named "Commission" with replication factor 2:
```bash
    ./kafka-topics.sh --create --topic Commission --bootstrap-server localhost:9092 --partitions 3 --replication-factor 2
```
7. Repeat step 3 with command:
```bash
    python3 producer2.py
```
8. Repeat step 4 with command on different terminal:
```bash
    python3 consumer2.py
```
9. Repeat step 5 to see a new Database.
```bash
    show  dbs
```
10. Now run third producer and consumer, Same as above in different terminals with creating a topic 'MarkUpPercentage' with replication factor 3:
```bash
    ./kafka-topics.sh --create --topic MarkUpPercentage --bootstrap-server localhost:9092 --partitions 3 --replication-factor 3
```
11. Check the database made in MongoDb same as above.






