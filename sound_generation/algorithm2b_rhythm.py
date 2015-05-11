import os
import time
import subprocess
import math
import random
from threading import Thread

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
csounds = 3

clines = [get_csound(math.ceil(x*csounds)) for x in lines]
slines = [get_sound(math.ceil(x*sounds)) for x in lines]

sleep = 0.5

iteration = 0

def thread1():
    for x in range(len(lines)):
        if lines[x] == 0: continue
        if lines[x] > 0.5:
            #print clines[x]
            subprocess.Popen(['afplay',clines[x]])
            time.sleep(1.5)
        else:
            continue

rhy = [0.3,0.3,0.3,2,0.3,0.3,0.3,0.3,2]

def thread2():
    for x in range(len(lines)):
        if lines[x] == 0: continue
        if lines[x] < 0.9:
            print slines[x]
            last = slines[x]
            subprocess.Popen(['afplay',slines[x],'-v','1'])
            sleep = rhy[x%len(rhy)]
            print sleep
            time.sleep(sleep)


th1 = Thread(target = thread1);
th2 = Thread(target = thread2);
th1.start()
th2.start()
th1.join()
th2.join()
