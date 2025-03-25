#Limit method of Estimation of Pi

import math #import the math library

n = 41354 #replace your number here

#it may happen that n is too large. So, we use try except block
try:
    #math.sin() takes radian values. so we calculate 180/n and make it radian.
    #this results in pi.
    val = n * math.sin(math.radians(180/n))


    print(val)

except OverflowError:
    print("Integer too large. Give something a little smaller.")#in case of error.
