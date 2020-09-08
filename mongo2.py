import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/palaniappan/Documents/dead_link/output1.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient("mongodb+srv://mongo_csv:SjP@cluster0.k6yd0.mongodb.net/mongo_csv?retryWrites=true&w=majority") 
db=mongo_client.mongo_csv
db.segment.drop()
header= [ "referer","status","url"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.segment.insert(row)