# **Check Point [Last : 91262]**
## Tool <br>
- python 3.7 
## Setup <br>
- set PIR from detect <br>
- set keypad for input <br>
- sniffing packet from bluetooth protocol<br>
- set MQTT publish from sent payload<br>
- set get payload from firebase <br>
- set JSON <br>
- set timestamp <br>
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
- listen PIR detect<br>
### PIR detect !!! <br>
- read old payload JSON from file 
- input phonenumber {size = 10}
- get data from firebase-realtime
- sent MQTT "topic:detail_user"
- next to sniffing
### sniffing packet from bluetooth 
- check data in packet != raw data in old payload<br>
# TO DO : WAIT EDIT MORE
- get select mode page + function select mode<br>
- get payload Student ID form firebase<br>
- set payload Student ID {weight , height , bmi} of firebase <b>"meaning real-time"</b> <br>
- get date from NTP Server when push json history <b>ONLY!</b> <br>
- push json history payload {weight , height , bmi} with Etag timestamp (yyyy-mm-dd'T'hh:mm:ss) from NTP Server <b>"meaning history"</b><br>
### Select mode <br>
- before select mode show welcome page<br>
- show select mode page <br>
- "A" to online <br> 
- "B" to offline <br>
- in 30 sec if nothing turn off led 
### Online <br>
- read SSID , Password from EEPROM
- if no wifi start wifimanager 
 > - get config wifi page {show SSID , Password for config} <br>
 > - start AP to config <br>
 > - get wifi connect when config finish <br>
- if have wifimanager going !! 
- get wifi connect when config finish
- ID input by keypad + get ID data from firebase 
 > - input can reset everytime
 > - if input > ID : can't input and process <br>
 > - if input != int : can't input process 
- show detail page user
- show weight {2 time to success} 
 > - no weight in 30 sec back to select mode
- height with input by keypad + push to height firebase  
 > - input can reset everytime
 > - if input > height (lock hundred point) : can't input and process 
 > - if input != int : can't input and process
- show results BMI with image 
> - bmi <= 18.5 {under}
> - bmi > 18.5 && bmi <= 22.9 {healthy}
> - bmi >= 23 && bmi <= 29.9 {over}
> - bmi > 29.9 {obese}
- set real-time , push history payload {weight , height , bmi} to firebase
- in 30 sec back to select mode
### Offline
- show weight {2 time to success}
> - no weight in 30 sec back to select mode
- height with input by keypad 
 > - input can reset everytime
 > - if input > height (lock hundred point) : can't input and process 
 > - if input != int : can't input and process
- show results BMI with image 
> - bmi <= 18.5 {under}
> - bmi > 18.5 && bmi <= 22.9 {healthy}
> - bmi >= 23 && bmi <= 29.9 {over}
> - bmi > 29.9 {obese}
- in 30 sec back to select mode

###### Last Commit : 161162
