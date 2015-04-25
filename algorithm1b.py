import os
import time
import subprocess
import math
with open('output4_n') as f:
    lines = f.readlines()

lines = map(str.strip,lines)
lines = map(float,lines)

rang = max(lines)

lines = [x/rang for x in lines]

def get_psound(number):
    return 'planet%03d.mp3'%(number+1)

def get_csound(number):
    return 'celesta%03d.mp3'%(number+1)

def get_wsound(number):
    return 'wikki%03d.mp3'%(number+1)

psounds = 32
csounds = 26
wsounds = 12

clines = [get_csound(math.ceil(x*csounds)) for x in lines]
plines = [get_psound(math.ceil(x*psounds)) for x in lines]
wlines = [get_wsound(math.ceil(x*wsounds)) for x in lines]

alllines = [lines,clines,plines,wlines]
#lines = [get_sound(x) for x in lines]

for x in range(len(lines)):
    if lines[x] == 0: continue
    print lines[x]
    if lines[x] < 1:
        print clines[x]
        subprocess.Popen(['afplay',wlines[x]])
    else:
        subprocess.Popen(['afplay',plines[x],'-v','0.2'])
    time.sleep(0.5)
    #subprocess.Popen(['afplay',x])
