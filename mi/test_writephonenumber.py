import os 
import readchar
#phonenumber = input("Enter Your Phonenumber : ")
#path = os.path.join(os.path.expanduser('/home/pi'), 'MagicMirror' , 'modules','default','helloworld','input_phonenumber.txt')
#f = open(path,"w+")
#f.write(phonenumber)
#f.close()
count = 0
phonenumber = ""
while count < 10:
    key = readchar.readkey()
    phonenumber += key
    path = os.path.join(os.path.expanduser('/home/pi'), 'MagicMirror' , 'modules','default','helloworld','input_phonenumber.txt')
    with open(path, 'a') as the_file:
        the_file.write(key+'\n')
    print(key)
    count = count + 1
print(phonenumber)
f = open(path,'a+')
f.truncate(0)

