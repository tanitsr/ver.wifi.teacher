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
publish.single("fromMachine",y,qos=2,hostname="35.192.38.248",port=1883,auth={'username':"pty7xkusrc"
,'password':"{pty7}xKUSRC"})


