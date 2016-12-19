#!/usr/bin/python
import os
import time
import blah

start = time.time()
for i in range(1000):
    rc = os.fork()
    if rc == 0:
        blah.f()
        exit()
    elif rc < 0:
        print "error!"
    else:
        continue
        os.wait()
end = time.time()
print end - start
