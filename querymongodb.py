import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = {"address": "Park Lane 38"}
myquery1 = {"address": {"$gt": "S"}} #$gt starts with letter S or higher
mydoc = mycol.find(myquery)
mydoc1 = mycol.find(myquery1)
for x in mydoc:
    print(x)
print("-------------------00")

for x in mydoc1:
    print(x)

myquery2 = {"address": {"$regex": "^S"}} #starts only with the letter S
mydoc2 = mycol.find(myquery2)

print("11111111111111111111111")
for x in mydoc2:
    print(x)

