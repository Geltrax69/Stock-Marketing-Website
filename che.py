class call:
    def make_call(self,name=None,mobile=None):
        self. name=name
        self. mobile=mobile
        print("caller name: ",self.name)
        print("mob no: " , self.mobile)
    def show_call(self):
        return [self.name,self.mobile]


n=input("name: ")
m=int(input("Mobile no: "))

c1=call()
c1.make_call(n)
c1.make_call(n)
print(c1.show_call())
print("text")
l=c1.show_call()
print(l[1])