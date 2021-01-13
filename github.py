from pymongo import MongoClient
import requests
import datetime, pprint

client = MongoClient()
db = client.test_database
collection = db.githubaccts

def find_user(username):
    response = requests.get(f'https://api.github.com/users/{username}')
    json = response.json()
    user_obj = {"username": username}
    user_obj["bio"] = json.get('bio')
    store_user(user_obj)
    return user_obj

def store_user(user_obj):
    collection.insert_one(user_obj)

print(find_user('sschneeberg'))
print(collection.find_one())
