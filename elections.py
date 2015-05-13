from random import randint #random
wins = 0 #variable wins 
for i in range(10000): # repeat 10000
  regions = 0 #varaible regions
  if randint(0,100)<= 87: #randomized number less than 87
    regions = regions +1 # added regions for wins 
  if randint(0,100)<= 65: #randomized number less than 65
    regions = regions +1 
  if randint(0,100)<= 17: #randomized number less than 17
    regions = regions +1
  if regions >= 2: # number of events won greater than/equal to 2
    wins = wins + 1 # whole win of elections +1 

percent = ((wins)/float(10000)) * 100 # percentage won
print "You have won the election %s percent of the time" %(percent) # inclusion of the percent into the end result 


  
