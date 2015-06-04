from gopigo import *
import time
from random import randint
enable_servo()
enable_encoders()
left_distance = 0
right_distance = 0
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

servo(90)
while 1<2:
  while us_dist(15) > 20:
    fwd()
  stop()
  servo(0)
  left_distance = us_dist(15)
  servo(180)
  right_distance = us_dist(15)
  if left_distance > right_distance:
    turn_left()
    servo(90)
  else:
    turn_right()
    servo(90)
