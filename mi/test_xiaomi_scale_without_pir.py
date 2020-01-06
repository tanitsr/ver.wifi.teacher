#!/usr/bin/python3
from __future__ import print_function
import argparse
import binascii
import os
import sys
from bluepy import btle
from datetime import datetime
import RPi.GPIO as GPIO
import time
import Xiaomi_Scale_Body_Metrics
import json 
import paho.mqtt.publish as publish
from datetime import datetime
import readchar
import smbus2 as smbus


MISCALE_MAC = '0C:95:41:B0:F6:DF'

if os.getenv('C', '1') == '0':
    ANSI_RED = ''
    ANSI_GREEN = ''
    ANSI_YELLOW = ''
    ANSI_CYAN = ''
    ANSI_WHITE = ''
    ANSI_OFF = ''
else:
    ANSI_CSI = "\033["
    ANSI_RED = ANSI_CSI + '31m'
    ANSI_GREEN = ANSI_CSI + '32m'
    ANSI_YELLOW = ANSI_CSI + '33m'
    ANSI_CYAN = ANSI_CSI + '36m'
    ANSI_WHITE = ANSI_CSI + '37m'
    ANSI_OFF = ANSI_CSI + '0m'


class ScanProcessor():
    def handleDiscovery(self, dev, isNewDev, isNewData):
        found = False
        if dev.addr == MISCALE_MAC.lower() and isNewDev:
            print ('    Device: %s (%s), %d dBm %s. ' %
                   (
                       ANSI_WHITE + dev.addr + ANSI_OFF,
                       dev.addrType,
                       dev.rssi,
                       ('' if dev.connectable else '(not connectable)'))
                   , end='')
            for (sdid, desc, data) in dev.getScanData():
                if sdid == 22:
                   print('')
                   print ('data:')
                   print (data)
                   user_payload["raw_data"] = data
                if data.startswith('1b18') and sdid == 22:
                    measunit = data[4:6]
                    measured = int((data[28:30] + data[26:28]), 16) * 0.01
                    unit = ''

                    if measunit == "03": unit = 'lbs'
                    if measunit == "02": unit = 'kg' ; measured = measured / 2
                    miimpedance = int((data[24:26] + data[22:24]), 16)

                    if miimpedance > 0 and miimpedance < 600 and lastpayload["raw_data"] != data:
                        print('')
                        print("weight : %.1f" % round(measured, 2))
                        print("impedance : %s " % miimpedance)
                        #payload[0] = round(measured, 2)
                        #payload[1] = miimpedance
                        user_payload["weight"] = round(measured, 2)
                        user_payload["impedance"] = int(miimpedance)
                        #print(user_payload["impedance"])
                        return
                    else:
                        print("Scale is sleeping.")                    
            if not dev.scanData:
                print ('\t(no data)')
            print

class keypad_module:

  I2CADDR    = 0x20   	# valid range is 0x20 - 0x27

  PULUPA = 0x0F		# PullUp enable register base address
  PULUPB = 0xF0		# PullUp enable register base address
  
  # Keypad Keycode matrix
  KEYCODE  = [['1','2','3','A'], # KEYCOL0
              ['4','5','6','B'], # KEYCOL1
              ['7','8','9','C'], # KEYCOL2
              ['*','0','#','D']] # KEYCOL3

  # Decide the row
  DECODE = [0,0,0,0,0,0,0,3,0,0,0,2,0,1,0,0]

  # initialize I2C comm, 1 = rev2 Pi, 0 for Rev1 Pi
  i2c = smbus.SMBus(1) 

  # get a keystroke from the keypad
  def getch(self):
    while 1:
        time.sleep(0.17)
        self.i2c.write_byte(self.I2CADDR, self.PULUPA)
        row = self.i2c.read_byte(self.I2CADDR)
        if (row) != 0b1111:
            self.i2c.write_byte(self.I2CADDR, self.PULUPB)
            col = self.i2c.read_byte(self.I2CADDR) >> 4
            row = self.DECODE[row]
            col = self.DECODE[col]
            return self.KEYCODE[row][col]

  # initialize the keypad class
  def __init__(self,addr):
    self.I2CADDR = addr





def pirDetection():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.IN)
    while True:
        if GPIO.input(16) == 1:
            print("Detect !!")
            return
        print("Not Detect !!")
        time.sleep(3)




def main():   
    while(True):
        scanner = btle.Scanner().withDelegate(ScanProcessor())
        print (ANSI_RED + "Scanning for devices..." + ANSI_OFF)
        devices = scanner.scan(3)
        #print("Past : %s" %lastpayload[1])
        #print("Last : %s" %payload[1])
        if(user_payload["impedance"] != lastpayload["impedance"] and user_payload["impedance"] > 0):
            print("compare")                     
            return
        
def getPhonenumber():
    count = 0
    number = ""
    keypad = keypad_module(0x20)    
    while True:
        key = keypad.getch()
        if(key == 'A'):
            print("input")         
            while True:
                key = keypad.getch()
                if(key != 'A' and key != 'D' and count < 10):                
                    number += key
                    path = os.path.join(os.path.expanduser('/home/pi'), 'MagicMirror' , 'modules','default','helloworld','input_phonenumber.txt')
                    with open(path, 'a') as the_file:
                        the_file.write(key+'\n')
                    print(key)
                    count = count + 1
                elif(key == 'A' and count == 10):
                    print("Next")
                    return number
                elif(key == 'D'):
                    print("Clear")
                    resetFile() 
                    count = 0
                    number = ""
        else:
            print("Plase ")


def writeJsonInFile():
    path = os.path.join(os.path.expanduser('/home/pi'), 'MagicMirror' , 'modules','default','helloworld','input.txt')
    with open(path,"w+") as outfile:
        json.dump(user_payload, outfile,indent=2)
    


def readLastJson():
    path = os.path.join(os.path.expanduser('/home/pi'), 'MagicMirror' , 'modules','default','helloworld','input.txt')
    with open(path) as json_file:
        lastpayload = json.load(json_file)
    return lastpayload

def resetFile():
    path = os.path.join(os.path.expanduser('/home/pi'), 'MagicMirror' , 'modules','default','helloworld','input_phonenumber.txt')
    f = open(path,'a+')
    f.truncate(0)



def metrics():
    metrics = Xiaomi_Scale_Body_Metrics.bodyMetrics(user_payload["weight"],user_payload["height"],user_payload["age"]
    ,user_payload["sex"],user_payload["impedance"])
    user_payload["bmi"] = round(metrics.getBMI(),2)
    user_payload["basal_metabolism"] = round(metrics.getBMR(),2)
    user_payload["visceral_fat"] = round(metrics.getVisceralFat(),2)
    user_payload["lean_body_mass"] = round(metrics.getLBMCoefficient(),2) 
    user_payload["body_fat"] = round(metrics.getFatPercentage(),2)
    user_payload["water"] = round(metrics.getWaterPercentage(),2)
    user_payload["bone_mass"] = round(metrics.getBoneMass(),2)
    user_payload["muscle_mass"] = round(metrics.getMuscleMass(),2)
    user_payload["protein"] = round(metrics.getProteinPercentage(),2)
    user_payload["type"] = "teacher"
   
    
def readFromFirebase():
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    if(not len(firebase_admin._apps)):    
        cred = credentials.Certificate("/home/pi/test-mainproject-2df90-firebase-adminsdk-eh0p3-4b9d683f80.json")
        default_app = firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://test-mainproject-2df90.firebaseio.com/'
        })
    ref = db.reference('/User')
    user_ref = ref.child(phonenumber)
    detail_user = user_ref.get()
    user_payload["first_name"] = detail_user["first_name"]
    user_payload["last_name"] = detail_user["last_name"]
    user_payload["weight"] = detail_user["last_weight"]
    user_payload["height"] = detail_user["last_height"]
    user_payload["age"] = detail_user["age"]
    user_payload["sex"] = detail_user["sex"]
    user_payload["phonenumber"] = phonenumber
    print(json.dumps(user_payload, indent=4))
    return

def writeRealTimeLoadToFirebase():
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    if(not len(firebase_admin._apps)):    
        cred = credentials.Certificate("/home/pi/test-mainproject-2df90-firebase-adminsdk-eh0p3-4b9d683f80.json")
        default_app = firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://test-mainproject-2df90.firebaseio.com/'
        })
    ref = db.reference('/User')
    user_ref = ref.child(phonenumber)
    user_ref.set({
        'first_name':user_payload["first_name"],
        'last_name':user_payload["last_name"],
        'sex':user_payload["sex"],
        'age':user_payload["age"],
        'last_weight':user_payload["weight"],
        'last_height':user_payload["height"]
    })

def sentDetailUserMQTT():
    x = {
        "name":user_payload["first_name"],
        "age":user_payload["age"],
        "sex":user_payload["sex"],
        "show":1
    }
    sent = json.dumps(x)
    publish.single("detail_user",sent,qos=2,hostname="127.0.0.1",port=1883,auth={'username':"username"
    ,'password':"raspberry"})

def sentPayloadUserMQTT():
    user_payload["show"] = 1    
    sent = json.dumps(user_payload)
    publish.single("payload_user",sent,qos=2,hostname="127.0.0.1",port=1883,auth={'username':"username"
    ,'password':"raspberry"})
    publish.single("fromMachine",sent,qos=2,hostname="35.192.38.248",port=1883,auth={'username':"pty7xkusrc"
    ,'password':"{pty7}xKUSRC"})

def sentProcessMQTT():
    x = {
        "process":"stop"
    }
    if user_payload["bmi"] == None:
        x["process"] = "running"
    sent = json.dumps(x) 
    publish.single("process",sent,qos=2,hostname="127.0.0.1",port=1883,auth={'username':"username"
    ,'password':"raspberry"})

def sentClearMQTT():
    x = {
        "show":0
    }
    sent = json.dumps(x)
    publish.single("detail_user",sent,qos=2,hostname="127.0.0.1",port=1883,auth={'username':"username"
    ,'password':"raspberry"})
    publish.single("payload_user",sent,qos=2,hostname="127.0.0.1",port=1883,auth={'username':"username"
    ,'password':"raspberry"}) 

if __name__ == "__main__":
    user_payload = {
        "raw_data":None,
        "first_name":None,
        "last_name":None,
        "phonenumber":None,
        "weight":None,
        "height":None,
        "age":None,
        "sex":None,
        "impedance":0,
        "bmi":None, 
        "basal_metabolism":None,
        "visceral_fat":None,
        "lean_body_mass":None,
        "body_fat":None,
        "water":None,
        "bone_mass":None,
        "muscle_mass":None,
        "protein":None,
        "type":None
    }
    
    while(True):
        lastpayload = readLastJson()
        print(lastpayload)
        #pirDetection()
        phonenumber = getPhonenumber()
        #phonenumber = input("Enter your phonenumber : ")
        readFromFirebase()
        sentDetailUserMQTT()
        sentProcessMQTT()    
        main()
        metrics()
        print(json.dumps(user_payload, indent=4))
        writeJsonInFile()
        ##writeRealTimeLoadToFirebase()
        sentProcessMQTT()
        sentPayloadUserMQTT()
        resetFile() 
        time.sleep(30)
        sentClearMQTT()

