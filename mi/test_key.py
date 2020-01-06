import smbus2 as smbus
import time
import os

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

def resetFile():
    path = os.path.join(os.path.expanduser('/home/pi'), 'MagicMirror' , 'modules','default','helloworld','input_phonenumber.txt')
    f = open(path,'a+')
    f.truncate(0)


# test code
def main():
  count = 0 
  keypad = keypad_module(0x20)
  ch = keypad.getch()
  if ch == 'A':
    print("Input")
    while count < 10:  
      ch = keypad.getch()
      print(ch)
      count = count + 1
      print("len : " ,count)
      path = os.path.join(os.path.expanduser('/home/pi'), 'MagicMirror' , 'modules','default','helloworld','input_phonenumber.txt')
      with open(path, 'a') as the_file:
        the_file.write(ch+'\n')
      if ch == 'D':
        resetFile()
        count = 0

# don't runt test code if we are imported
if __name__ == '__main__':
  main()