from pymongo import MongoClient
uri ="mongodb+srv://Demo:Demo_123@cluster0.9sjlmqh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client. college # college is a collection name
students= list(db["students"].find(limit=100))
print(students)