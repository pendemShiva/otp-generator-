from OtpGenrator import *
class Verification(OtpGenrator):
    def otpchecking(self,noTimeOtp=4):
        for i in range(1,noTimeOtp):
            userEntered=input('enter the otp you received')
            if(userEntered==self.sentOTP):
                print('you are successfully entered to our website')
                break
            else:
                print(f'incorrect password please enter gain.you have  {3-i} chance')
                    
        else:
            print('you have exceded maximum limit try after some time')
