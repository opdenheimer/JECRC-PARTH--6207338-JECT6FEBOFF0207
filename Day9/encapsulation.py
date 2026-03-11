'''
Encapsulation:
it is used to provide security to the data(data means variables/prop &methods present inside a class)
To provide data security we use Access Specifiers: Access Specifiers describe who can access the class members
(Properties& methods)  

1.Public
2.Protected
3.Private

'''

#Public Specifiers
# class Temp:
#     a,b,*c,d="HELLO"

#     def greeting(self):
#         print("Good Afternoon:)")

# class C2(Temp):
#     pass

#protected Member
# class Pr1:
#     #soft barrier as still it acts as a public member in python
#     _a=10  #here '_' added infornt of a var denotes a protected 
#     _b="I Love YOU"

# obj1= Temp()
# print(obj1._b)
# print(obj1._a)

#Private Members
'''
can access private members with 
1. By using Syntax
2. get & set method
3. by using @property decorator
'''
class Temp:
    __a=123   #here '__' added infornt of a var denotes a private
    
    def __status(self):
        print("Class name in Temp!")

    def get(self):
        print(self.__a)

    def set(self,new_val):
        self.__a=new_val   

    @property
    def get1(self):
        print(self.__a)    

    @get1.setter
    def set1(self,new_val):
        self.__a=new_val       

# obj=Temp()
# print(obj.__prew)
# obj.__status()   wont work

#By using syntax
''' 
obj_name/cls_name._CN__prop_name/__method_name(Accessing) 
obj_name/class_name._CN__memberName=NewValue(Modifing)
'''
# def new_method():
#     print("I have found the variable")

# print(obj._Temp__a)
# print(Temp._Temp__a)
# obj._Temp__status()

#By using get & set methods
# obj=Temp()
# obj.get()
# obj.set(1)
# obj.get()
# print(obj._Temp__a)

#By using Property Decorator

obj=Temp()
obj.get1
obj.set1=3121
obj.get
print(obj._Temp__a)

