from profile import *
from Verification import  *
#object creation
k=profile()
objjverfi=Verification()
#method calling
MobileNo=k.getMobileNo()

result=objjverfi.mobileNumberCheck(MobileNo)
# mobile number verfication
if(result!=0):
    k.views()
    objjverfi.randomNumberPick()
    objjverfi.generator()
    objjverfi.otpchecking()
else:
    print('enter the vaild 10 digit mobile number')
    result=objjverfi.mobileNumberCheck(MobileNo)
    

