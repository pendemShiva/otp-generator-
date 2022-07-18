class profile:
    def __init__(self):
        self.name=input("enter your Name")
        self.fname=input('enter your father name')
        self.mobileno=input('enter the number')
    def views(self):
        print('your mobile number is',self.mobileno)
    def getMobileNo(self):
        return self.mobileno
