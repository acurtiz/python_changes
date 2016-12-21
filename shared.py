#!/usr/bin/python
import os
import time
import lambda_func

def Checkpoint():
    lambda_func._CHECKPOINT_ = 1
def Restore():
    lambda_func._RESTORE_ = 1

start = time.time()
for i in range(1000):
    Checkpoint()
    lambda_func.f()
    Restore()
end = time.time()

print end - start
