def checkpoint():
    import testImport
    testImport._START_FREEZE_ = 1

def restore():
    import testImport
    testImport._SPECIAL_ = 1

 import os

 def lambdaFunc():
     os.open = 3

 print os.open  # output: <built-in function open>
 checkpoint()
 lambdaFunc()
 restore()
 print os.open  # output: <built-in function open>







checkpoint()
restore()
print os.open  # output: <built-in function open>

