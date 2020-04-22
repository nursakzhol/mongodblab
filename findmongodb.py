import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
#returns the first occurance in the selection
x = mycol.find_one()

print(x)