'''
Custom Exception:
we use prebuilt exception class name according to our requirement
raise ValueError('message)

valueE
'''
# num=16
# if num>=18:
#     print("You are an adult")
# else:
#     raise NameError("Age should be greater than equals to 18!")    


class MyException(Exception):
    pass
 #raise MyException('This is my exception class!')


n1,n2=10,3

if n2==0:
    raise MyException('Second num cant be zero')
else:
    print(n1/n2)


'''
Assertion Error:
--Assertion exception canbe created by using one keyword called "assert"

assert<condition>,print(ERROR)
print(output)
'''    
s=input('Enter a string:')
assert s==s[::-1],print("it is not a palindromic String!")
print("it is a palindromic string!")


  