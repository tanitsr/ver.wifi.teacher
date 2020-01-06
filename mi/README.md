# **Check Point [Last : 060362]**
## Tool <br>
- python 3.7 
## Setup <br>
- set keypad for input <br>
- sniffing packet from bluetooth protocol<br>
- set MQTT publish from sent payload<br>
- set get payload from firebase <br>
- set JSON <br>
### Import
- argparse
- binascii
- os
- sys
- RPi.GPIO as GPIO
- time
- Xiaomi_Scale_Body_Metrics
- json 
- paho.mqtt.publish as publish
- readchar
- smbus2 as smbus
### From
- bluepy import btle
- datetime import datetime
- datetime import datetime

## Function <br>
### input , write file , read file
- press "A" for input number
- enter input number from keypad {size = 10}
>- number write to input.txt
>- press "A" for input is done 
>- press "D" for clear
- read old payload JSON from file
### read data with path{phonenumber} from RTDB
- get data from firebase-realtime
- sent payload to MagicMirror via MQTT "topic:detail_user"
- next to sniffing
### sniffing packet from bluetooth 
- check data in packet != raw data in old payload<br>
>- "true" next step 
>- "false" loop 
- get weight and impedacen from bluetooth 
### calculation body values
- save in user_payload JSON wait using in function metrics
- call metrics function for calculation body values and save body values in user_payload JSON
### sent payload to MagicMirror via MQTT
- sent payload to MagicMirror for show result  "topic:payload_user"
### sent payload to GCP via MQTT
- set sent payload and sent to GCP via MQTT "topic:fromMachine"
### Delay 
### sent payload via MQTT
- sent payload for clear screen MagicMirror  "topic:detail_uesr , payload_user"

###### Last Commit : 060163
