import testImport
import pprint
import sys
import os
pp = pprint.PrettyPrinter(indent=4)

def x():
    return 'Im a string! x() just returned me!'

def printSpecialDict():
    print 'Printing special dict: '
    pp.pprint(globals()['_SPECIAL_'])

def printChanged(name, oldval, newval):
    print 'Changed ' + name + ' from ' + str(oldval) + ' to ' + str(newval)

# to freeze, we just need to make sure _SPECIAL_ actually exists (auto-record if it exists)
def FREEZE(): 
    print '##############'
    print '#### Freezing, i.e. recording changes in special dictionary now'
    print '##############'
    global _SPECIAL_
    _SPECIAL_ = {}

# if any attribute is called _SPECIAL_ and is set, cpython function unrolling changes is called... change later
def UNFREEZE():
    print '##############'
    print '#### Unfreezing, i.e. rolling back changes'
    print '##############'
    testImport._SPECIAL_ = 1

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
print 'sys.open is now: ' + str(sys.byteorder)
print 'sys.exc_info is now: ' + str(sys.exc_info)
print 'testImport.check is now: ' + str(testImport.check)

print 'Does _SPECIAL_ dictionary exist in globals anymore? Checking... ' + str('_SPECIAL_' in globals())

# NOTE: the following doesn't work - apparently globals() are global only within a module
'''
print 'Now going to try importing a module that actually imports a built-in and changes its value'
print 'os.open is: ' + str(os.open)
FREEZE()
print globals()
print '.....................................................'
import testImport2
print os
printSpecialDict()
UNFREEZE()
print 'os.open is: ' + str(os.open)
'''
