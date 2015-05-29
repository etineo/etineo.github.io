from gopigo import *
import time
from random import randint

distance_to_stop=20
print "Press ENTER to Start"
raw_input()
fwd()

def turn_right():
  enc_tgt(1,0,15)
  time.sleep(.1)
  right()
  time.sleep(2)

def turn_left():
  enc_tgt(0,1,15)
  time.sleep(.1)
  left()
  time.sleep(2)
  
while 1<2:
  while us_dist(15) > 20:
    print "Dist:", dist,'cm'
    fwd()
  stop()
  if randint(0,1) == 0:
    turn_left()
  else:
    turn_right()
