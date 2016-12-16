import os
os.open = 4
print 'Inside testImport2, just changed os.open'
print globals()
