#!/usr/bin/python
import os
import time
import lambda_func

def Checkpoint():
    blah._CHECKPOINT_ = 1
def Restore():
    blah._RESTORE_ = 1

start = time.time()
for i in range(1000):
    Checkpoint()
    lambda_func.f()
    Restore()
end = time.time()

print end - start
