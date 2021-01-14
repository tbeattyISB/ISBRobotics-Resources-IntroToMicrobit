from microbit import *

# Define the motor class and run command for using Maqueen
class Motor:
 def __init__(self,motornum,switch_polarity=False):
  if(motornum==1):
   self._motornum=0
  elif(motornum==2):
   self._motornum=2
  else:
   raise(ValueError('Maqueen only has motors 1 and 2 not ',motornum))
  self._switch_polarity=switch_polarity
 def run(self,power):
  direction=0
  raw_power=int(round(2.55*abs(power)))
  if(power<0):
   direction=1
   if(power<-100):
    raw_power=255
  elif(power>100):
   raw_power=255
  rlist=[self._motornum,direction,raw_power]
  try:
   i2c.write(0x10,bytes(rlist))
  except:
   print('Maqueen not connected?')
   display.show(Image.NO)

# Define the left and right motor
leftMotor = Motor(1)
rightMotor = Motor(2)

# Set the motor to stopped in case the motor was running when reset
leftMotor.run(0)
rightMotor.run(0)

# Start forever loop
while True:
    if button_a.was_pressed():
        display.show(Image.HEART) #Show button was clicked
        sleep(1000)       # Wait a bit to have robot set
        leftMotor.run(50) # Run motor at 50%
        sleep(2000) 
        leftMotor.run(0)
        display.clear()
