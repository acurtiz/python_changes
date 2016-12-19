#!/usr/bin/python
import os
import time
import blah

start = time.time()
for i in range(1000):
    #blah = reload(blah)
#    import blah
    blah.f()
end = time.time()
print end - start
