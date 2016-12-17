import os
os.open = 4
print 'Inside testImport2, just changed os.open'

# comment out the following and specifically look at the output from printing the special dictionary; you'll see the artifacts
# (but we account for them when applying the changes, although not sure if that is correct)
'''
print globals # having this here causes some odd artifacts unless we explicitly check if each key is a module object 
import testImport
testImport._PRINT_SPECIAL_ = 3
'''
