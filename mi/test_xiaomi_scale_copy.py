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
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

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
        if(user_payload["impedance"] != 0 and user_payload["impedance"] > 0):
            print("compare")                     
            return
        
   


def writeFile():
    path = os.path.join(os.path.expanduser('/home/pi'), 'MagicMirror' , 'modules','default','helloworld','input.txt')
    file1 = open(path,"w+")
    file1.write("Weight : "+str(payload[0]) + "\n" + 
    "Height : " + str(payload[2]) + "\n" + 
    "BMI : " + str(payload[3]) + "\n" + 
    "Basal Metabolism : " + str(payload[4]) + "\n" +
    "Visceral Fat : " + str(payload[5]) + "\n" +
    "Lean Body Mass : " + str(payload[6]) + "\n" +
    "Body Fat : " + str(payload[7]) + "\n" +
    "Water : " + str(payload[8]) + "\n" +
    "Bone Mass : " + str(payload[9]) + "\n" +
    "Muscle Mass : " + str(payload[10]) + "\n" +
    "Protein : " + str(payload[11]) + "\n" + 
    str(payload[0]) + "\n" + str(payload[1])
    )
    file1.close()
    #goto[0] = True
    return

def writeJsonInFile():
    path = os.path.join(os.path.expanduser('/home/pi'), 'MagicMirror' , 'modules','default','helloworld','input.txt')
    with open(path,"w+") as outfile:
        json.dump(user_payload, outfile,indent=2)
    


def readLastJson():
    path = os.path.join(os.path.expanduser('/home/pi'), 'MagicMirror' , 'modules','default','helloworld','input.txt')
    with open(path) as json_file:
        lastpayload = json.load(json_file)
    return lastpayload





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
    
def readFromFirebase():
    phonenumber = input("Enter your phonenumber : ")
    cred = credentials.Certificate("/home/pi/test-mainproject-2df90-firebase-adminsdk-eh0p3-4b9d683f80.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://test-mainproject-2df90.firebaseio.com/'
    })
    ref = db.reference('/User')
    user_ref = ref.child(phonenumber)
    detail_user = user_ref.get()
    user_payload["first_name"] = detail_user["first_name"]
    user_payload["last_name"] = detail_user["first_name"]
    user_payload["weight"] = detail_user["last_weight"]
    user_payload["height"] = detail_user["last_height"]
    user_payload["age"] = detail_user["age"]
    user_payload["sex"] = detail_user["sex"]
    print(json.dumps(user_payload, indent=4))



if __name__ == "__main__":
    payload = [0,0,0,0,0,0,0,0,0,0,0,0]
    user_payload = {
        "raw_data":None,
        "first_name":None,
        "last_name":None,
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
        "protein":None 
    }
    while(True):
        lastpayload = readLastJson()
        print(lastpayload)
        pirDetection()
        readFromFirebase()    
        main()
        metrics()
        print(json.dumps(user_payload, indent=4))
        writeJsonInFile() 

