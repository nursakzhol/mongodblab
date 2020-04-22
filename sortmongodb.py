import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name") #sort the result alphabetically by name
#we can use -1 for descending 
for x in mydoc:
    print(x)