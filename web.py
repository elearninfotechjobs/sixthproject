class data:
        sc='xyz school'
        def __init__(self,name,rno):
                self.name=name
                self.rno=rno
        def m(self): #instance method
                print(self.name)
                print(self.rno)
        @classmethod                
        def n(cls):
                print(data.sc)
                print(cls.sc)
        @staticmethod               
        def p(x,y):
                print(x+y)
             

obj=data('abc',1001)
obj.m()
obj.n()
obj.p(10,20)


