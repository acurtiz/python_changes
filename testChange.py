import testImport
import pprint
import sys

_SPECIAL_ = {}
pp = pprint.PrettyPrinter(indent=4)

def x():
    return 'Im a string! x() just returned me!'

def printSpecialDict():
    print 'Printing special dict: '
    pp.pprint(globals()['_SPECIAL_'])

def printChanged(name, oldval, newval):
    print 'Changed ' + name + ' from ' + str(oldval) + ' to ' + str(newval)

def FREEZE(): 
    print '##############'
    print '#### Freezing, i.e. recording changes in special dictionary now'
    print '##############'
    _SPECIAL_ = {}

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

print '\n############################'
print 'Going to try and print special dictionary - expect an error because rolling back changes should have deleted it from global dictionary'
print '#############################'
printSpecialDict()
