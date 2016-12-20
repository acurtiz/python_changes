import time
import blah

t1 = time.time()
#blah._START_FREEZE_ = 1
import changer
#blah._SPECIAL_ = 1
t2 = time.time()

print t2 - t1
