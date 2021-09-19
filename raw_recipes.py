from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
from urllib.parse import parse_qs
line = "&time=1561768216000&gameCategory=PINPOINT&category=ONE&uniqueId=2518Z-0892A-0030O-16H70&transactionType=CRD&familyId=000-222-115-11119&realTs=1561768319000&sortId=1&msg=SET-UP+PRAYER+%26+intercession+begins+in+just+30+minutes.&remoteIpAddress=127.0.0.1&userAgent=HTTP&uniqueId=872541806296826880&time=1571988786000&gameCategory=NOTIFY&category=TWO&transactionType=CRD&familyId=401-222-115-89387&sortId=1&realTs=1571988989000&msg=This-is+a+reminder.&remoteIpAddress=127.0.0.1&userAgent=HTTPS&"

o = parse_qs(line)

print(o)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number' : e}
    producer.send('numtest', value=data)
    sleep(5)


consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('localhost:27017')
collection = client.numtest.numtest

for message in consumer:
    message = message.value
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))