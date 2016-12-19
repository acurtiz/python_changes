#!/usr/bin/python
import os
import time
import blah

start = time.time()
for i in range(1000):
    blah._START_FREEZE_ = 1
    blah.f()
    blah._SPECIAL_ = 1
end = time.time()

print end - start
