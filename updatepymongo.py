import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}

mycol.update_one(myquery, newvalues)

for x in mycol.find():
    print(x)

print("--------------")
#to update all documnets that starts with the letter S

myquery1 = {"address" : {"$regex": "^S"}}
newvalues1 = {"$set": {"name": "Minnnie"} }

x = mycol.update_many(myquery1, newvalues1)

print(x.modified_count, "documents updated.")