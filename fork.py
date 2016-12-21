#!/usr/bin/python
import os
import time
import lambda_func

start = time.time()
for i in range(1000):
    rc = os.fork()
    if rc == 0:
        lambda_func.f()
        exit()
    elif rc < 0:
        print "error!"
    else:
        continue
for i in range(1000):
    os.wait()
end = time.time()
print end - start
