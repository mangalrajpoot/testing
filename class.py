class abc:
    def add(self):
        self.d=int(input('Enter First Value'))
        self.e=int(input('Enter Second Value'))
        self.f=self.d+self.e
        print(self.f)
        

    

obj=abc() #object creation 
obj.add() #method calling

