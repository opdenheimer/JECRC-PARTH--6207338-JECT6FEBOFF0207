#inheritance
'''
1.single level
2. multilevel
3. multiple
4.hybrid
'''

#single Level
#we will have a single parent & child class also properties will be derived only one time

#Parent/Super Class
#class from which we are deriving properties is parent class
class Parent:
    bank_balance='54l'

    def __init__(self,members):
        self.members=members
        
    def desc(self):
        print("I am parent class")

#child/subclass
#Class in which we are going to derive the properites of the parent class is child class 
class Child(Parent):
    pass
    # def __init__(self,child_name,*args):
    #     self.child_name=child_name
    #     super().__init__(args)

    # def display(self):
    #     super().desc()    

obj=Child("cls2")
print(obj.members)
obj.desc()

#multi level inheritence
class p1:
    a="class1"
class p2(p1):
    b="class2"
class p3(p2):
    c="class3"
class p4(p3):
    d="class4"

#multiple inheritence
class p1:
    a="class1"
class p2:
    b="class2"
class p3:
    c="class3"
class p4:
    d="class4"
class childcls(p1,p2,p3,p4):
    pass    

print(childcls.a,childcls.b,childcls.c,childcls.d)