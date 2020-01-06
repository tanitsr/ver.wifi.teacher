import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random

if(not len(firebase_admin._apps)):    
        cred = credentials.Certificate("/home/pi/test-mainproject-2df90-firebase-adminsdk-eh0p3-4b9d683f80.json")
        default_app = firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://test-mainproject-2df90.firebaseio.com/'
        })
ref = db.reference('/User/student/a_1')
user_ref = ref.child('1_2')
user_ref.set({
    '001':{
        'first_name':'เจนยุทธ',
        'last_name':'รุ่งเกียรติวานิช',
        'sex':'male',
        'age': random.randint(4,5),
        'last_weight':random.randint(14,15),
        'last_height':random.randint(101,106)
    },
    '002':{
        'first_name':'ฐิติวัสส์',
        'last_name':'คริสตไทย',
        'sex':'male',
        'age': random.randint(4,5),
        'last_weight':random.randint(14,15),
        'last_height':random.randint(101,106)
    }, 
    '003':{
        'first_name':'ณัฐพงษ์',
        'last_name':'พนากิจสวัสดิ์',
        'sex':'male',
        'age': random.randint(4,5),
        'last_weight':random.randint(14,15),
        'last_height':random.randint(101,106)
    }, 
    '004':{
        'first_name':'ณัฐวุฒิ',
        'last_name':'รอดทองคำ',
        'sex':'male',
        'age': random.randint(4,5),
        'last_weight':random.randint(14,15),
        'last_height':random.randint(101,106)
    }, 
    '005':{
        'first_name':'ณิฌา',
        'last_name':'ศิริวงษ์',
        'sex':'female',
        'age': random.randint(4,5),
        'last_weight':random.randint(14,15),
        'last_height':random.randint(101,106)
    }, 
    '006':{
        'first_name':'ธนกร',
        'last_name':'แก้วทิม',
        'sex':'male',
        'age': random.randint(4,5),
        'last_weight':random.randint(14,15),
        'last_height':random.randint(101,106)
    }, 
    '007':{
        'first_name':'นวพล',
        'last_name':'ยุพา',
        'sex':'male',
        'age': random.randint(4,5),
        'last_weight':random.randint(14,15),
        'last_height':random.randint(101,106)
    },
    '008':{
        'first_name':'ปภัสรา',
        'last_name':'พวงทับทิม',
        'sex':'female',
        'age': random.randint(4,5),
        'last_weight':random.randint(14,15),
        'last_height':random.randint(101,106)
    }, 
    '009':{
        'first_name':'ปรีชญา',
        'last_name':'หลำดารา',
        'sex':'female',
        'age': random.randint(4,5),
        'last_weight':random.randint(14,15),
        'last_height':random.randint(101,106)
    },
    '010':{
        'first_name':'ปิยพนธ์',
        'last_name':'สุนทรวงศ์',
        'sex':'male',
        'age': random.randint(4,5),
        'last_weight':random.randint(14,15),
        'last_height':random.randint(101,106)
    },       
})