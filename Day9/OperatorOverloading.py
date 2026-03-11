'''
Operator Overloading:Phenomenon of making the operators to work on user-defined data types by invoking 
respective magic methods.

--Magic Methods/Dunder : Special Types of Methods in which '__' will be there at the starting and ending of the 
methods's name.

--eg
__add__,__sub__,__mul__
__floordiv__, __truediv__,__mod__

--If we don't use operator Overloading then : For using Operators inside user-defined data types we have to use
  operator overloading.

-- Syntax:
     class ClassName:
        def __init__(self, val):
           self.val=val

        def __add__(self,another_obj):
            return self.val +another_obj.val

      obj1=ClassName(val1)
      obj2=ClassName(val2)
      print(obj1+obj2)--> obj1.__add__(obj2)  

'''
class mydt:
    def __init__(self,val):
        self.val=val
    
    def __str__(self):
        return str(self.val)
    
    def __add__(self,*args):
        sum=self.val
        for i in args:
            sum+=i.val
        return mydt(sum)
    # def __add__(self,another_obj):
    #     return self.val+ another_obj.val
    
    def sub(self,*args):
        subs=self.val
        for i in args:
            subs-=i.val
        return subs
    def __sub__(self,another_obj):
        return self.val-another_obj.val
    
    def mul(self,*args):
        multi=self.val
        for i in args:
            multi+=i.val
        return multi
    def __mul__(self,another_obj):
        return self.val*another_obj.val
    
    def flrdiv(self,*args):
        fldiv=self.val
        for i in args:
            fildiv/=i.val
        return fildiv
    def __floordiv__(self, other):
        return self.val// other.val
    
    def trudiv(self,*args):
        trdiv=self.val
        for i in args:
            trdiv+=i.val
        return trdiv
    def __truediv__(self, other):
        return self.val/other.val
    

    def __mod__(self, other):
        return self.val%other.val


obj1=mydt(9)
obj2=mydt(2)

print( mydt(3)+mydt(2)+ mydt(21))
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1 //obj2)
print(obj1 / obj2)
print(obj1 % obj2)
