#!/usr/bin/python
import os
import time
import blah

def Checkpoint():
    blah._START_FREEZE_ = 1
def Restore():
    blah._SPECIAL_ = 1

start = time.time()
for i in range(1000):
    Checkpoint()
    blah.f()
    Restore()
end = time.time()

print end - start
