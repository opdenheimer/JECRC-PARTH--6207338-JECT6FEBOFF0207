import time

'''
Exception:
Unauthorized event which can hinder our flow of exection pf the program , after which it will not get executed 
-Syntax Error: when there is spelling or indentation mistake

-some approaches of handling Exeption:
-Specific Exception handling:
-
-


-Try: in try block we put normal line of code  or the problem statement we want to get executed but it might
have error in it so to prevent from code execution getting stop we use it if any error occurs it wont stop instead
would switch other conditions mentioned below 

-else: an alternative block of code after try if any error occurs in try block instead of getting tht error this 
block code will be getting executed . if error in try then go to else block , even if the code in else is correct 
then it would give the output but if error in else then would have an error but to overcome this we do have further 
handling techniques.

-except: in  except block we put actual soln for the error , if we encounter any error the soln to it is written over 
here (like in else block just to avoid code execution we wrote a diversion )

-finally : After getting error or after resolution , forcefully if we want to execute any particular block of code we use
finally block 


'''

#Specific exception handling : 
# print(10/0)
'''
try:
   error prone code
except:
   solution code   

'''

# n1,n2=10,0
# try:
#     result=n1/n2
#     print(result)
# except ZeroDivisionError:
#     print("do not divide with zero")

try:
    a,b,c=1,2
except ValueError:
    print("For performing MVC variable should be equal to no of values! ")

try:
    print(a,b,c)
except NameError:
    print("Identifiers not assigned values")

#Generic Exception Handling
'''
approach in which there is no need to pass any particular exception class name. insted we can just import a class
named exception which already containes parent exception class
Drawback: but it cant handle keyboard interupt 
'''
# try:
#     while True:
#         print(time.time())
# except Exception:
#     print("loop get stopped")        

#handling by specific handling
# try:
#     while True:
#         print(time.time())
# except KeyboardInterrupt:
#     print("loop get stopped")    

#Default Exception Handling
'''
It is a type of exception handling in which we can handle all types of errors or exception except "SyntaxError"
'''
try:
    while True:
        print(time.time())
except :
    print("loop get stopped")            