import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

""" name = 'boonboy'
cred = credentials.Certificate("/home/pi/test-mainproject-2df90-firebase-adminsdk-eh0p3-4b9d683f80.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-mainproject-2df90.firebaseio.com/'
})

ref = db.reference('/User')
user_ref = ref.child('0987654321')
user_ref.update({
    'user_first_name': name
})

print(user_ref.get()) """


num = 50
x = {
    "weight": num,
    "name": "godis"
}

print(x["weight"])