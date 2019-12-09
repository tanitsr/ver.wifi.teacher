import paho.mqtt.publish as publish
import json

x = {
    "name":"John",
    "age":18,
    "weight":3663636363,
    "phonenumber":"0987654321",
    "sex":"male",
    "show":0,
    "raw_data":3434434
}

user_payload = {
    "bmi":12
}

if user_payload["bmi"] != None:
    x["process"] = "esese"

y = json.dumps(x)
print(y)
publish.single("payload_user",y,qos=2,hostname="127.0.0.1",port=1883,auth={'username':"username"
,'password':"raspberry"})