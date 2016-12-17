import testImport
import pprint
import sys
import os
pp = pprint.PrettyPrinter(indent=4)

STORE_IN_INTERPRETER = True

def x():
    return 'Im a string! x() just returned me!'

def printSpecialDict():
    if (False):
        print 'Printing special dict: ' 
        if (STORE_IN_INTERPRETER): # store in interpreter sysdict
            testImport._PRINT_SPECIAL_ = 1
        else:  # store in per-module globals()
            if '_SPECIAL_' not in globals():
                print 'special dict doesnt exist in globals'
                return
            pp.pprint(globals()['_SPECIAL_'])

def printChanged(name, oldval, newval):
    print 'Changed ' + name + ' from ' + str(oldval) + ' to ' + str(newval)

# to freeze, we just need to set an attribute called _START_FREEZE_ on anything
def FREEZE(): 
    print '##############'
    print '#### Freezing, i.e. recording changes in special dictionary now'
    print '##############'
    testImport._START_FREEZE_ = 1

# to unfreeze (roll back changes), just need to set an attribute called _SPECIAL_ on anything
def UNFREEZE():
    print '##############'
    print '#### Unfreezing, i.e. rolling back changes'
    print '##############'
    testImport._SPECIAL_ = 1


### TEST CASE 1 (change stuff locally)
FREEZE()
print 'Changing a bunch of stuff in built-in sys, and imported module testImport'
old_sysbyteorder = sys.byteorder
old_sysexc_info = sys.exc_info
old_testImportcheck = testImport.check
sys.byteorder = 3
sys.exc_info = x
testImport.check = 5

printChanged('sys.byteorder', old_sysbyteorder, sys.byteorder)
printChanged('sys.exc_info', old_sysexc_info, sys.exc_info)
printChanged('testImport.check', old_testImportcheck, testImport.check)
printSpecialDict()

UNFREEZE()
print 'sys.byteorder is now: ' + str(sys.byteorder)
print 'sys.exc_info is now: ' + str(sys.exc_info)
print 'testImport.check is now: ' + str(testImport.check)

### TEST CASE 2 (import a module which changes something)
print '\n\nNow going to try importing a module that actually imports a built-in and changes its value'
print 'os.open is: ' + str(os.open)
FREEZE()
import testImport2
printSpecialDict()
print 'os.open is: ' + str(os.open)
UNFREEZE()
print 'os.open is: ' + str(os.open)

