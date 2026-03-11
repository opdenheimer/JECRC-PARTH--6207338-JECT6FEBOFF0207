"""
Hinding the implementation form user while showing only the required functionalities

Abstract Method:
if a method function consists of only declaration not defination then it will be called as "Abstract Method"

Abstract Class:
if a class consists of atleast one abstract method , it will be called as "Abstract Class".

Concret Class:
It consist of zero abstract method 

abc: Module
ABC: Abstract Base Class 
"""
from abc import ABC , abstractmethod

class ATM(ABC):
    @abstractmethod
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

class SBI_ATM(ATM): #concrete Class
    def generate_pin(self):
        print("Used to Generate ATM pin")

    def check_balance(self):
        print("your acc is empty earn some")

    def forget_pin(self):
        print("Not able to remember the pin! Then Forget now! ")

    def deposit(self):
        print("Save your money by giving it to me! ")

    def deposit(self):
        print("Has been deposited")

    def withdraw(self):
        print("dont withdraw money") 

obj=SBI_ATM()
obj.check_balance()
obj.deposit()
obj.forget_pin()
obj.generate_pin()
obj.withdraw()            
