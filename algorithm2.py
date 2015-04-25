import os
import time
import subprocess
import math
import random
with open('data') as f:
    lines = f.readlines()

lines = map(str.strip,lines)
lines = map(float,lines)

minimum = min(lines)
maximum = max(lines)
rang = -minimum+maximum

lines = [(x-minimum)/rang for x in lines]

def get_sound(number):
    return '%d.mp3'%(number+1)

def get_csound(number):
    return 'c%d.mp3'%(number+1)

sounds = 5
csounds = 4

clines = [get_csound(math.ceil(x*csounds)) for x in lines]
slines = [get_sound(math.ceil(x*sounds)) for x in lines]

#lines = [get_sound(x) for x in lines]

sleep = 0.5

iteration = 0

for x in range(len(lines)):
    if lines[x] == 0: continue
    #print lines[x]
    print lines[x]
    ty = True
    if lines[x] < 0.4:
        print clines[x]
        subprocess.Popen(['afplay',clines[x]])
        time.sleep(0.3)
    else:
        ty = False
        print slines[x]
        subprocess.Popen(['afplay',slines[x],'-v','1'])
        time.sleep(0.7)
    iteration += 1
    if iteration > 3:
        iteration = 0
        sleep = random.random()
    #time.sleep(sleep)
    #subprocess.Popen(['afplay',x])
