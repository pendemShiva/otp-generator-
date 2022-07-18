from random import randrange
from random import choice
class OtpGenrator:
    listOfValues=['4257','6491','97123','3539']
    noOfDigts=['self.firstNumber','self.secoundnumber','self.thirdnumber','self.fourth']
    def randomNumberPick(self):
        for i in OtpGenrator.noOfDigts:
            selectedlist=choice(OtpGenrator.listOfValues)
            exec("%s = %d" % (i,randrange(int(selectedlist[0:2]),int(selectedlist[2:]))))
    def generator(self):
        self.sentOTP=chr(self.firstNumber)+chr(self.secoundnumber)+chr(self.thirdnumber)+chr(self.fourth)
        print('OTP is',self.sentOTP)
        print('OTP sent successfully')
        return self.sentOTP
