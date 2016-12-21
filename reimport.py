#!/usr/bin/python
import os
import time
import lambda_func

start = time.time()
for i in range(1000):
    lambda_func = reload(lambda_func)
    lambda_func.f()
end = time.time()
print end - start
