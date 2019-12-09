from datetime import datetime
#now = datetime.now()
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d'T'%H:%M:%S")
print("Current Time =", dt_string)
