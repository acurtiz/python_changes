import testImportNest
print 'Inside testImport3, just imported testImportNest'
print 'testImportNest.x is: ' + str( testImportNest.x)
testImportNest.x = 5 # it was 99
print 'Changed testImportNest.x to ' + str(testImportNest.x)
