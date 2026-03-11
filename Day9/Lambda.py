"""
1.Lambda is a keyword Which is used to create anonymous functions.
2. For calling the lambda Function we can store the address of lambda inside a variable . by invoking the var_name
 , we can call the function. 
"""
## lambda args:<exp>
# result= lambda a,b :a+b ##returns value
# print(result)
# print(result(1,3))
# #lambda 
# (lambda a,b: print(a+b))(int(input("enter first no:")),int(input("enter second no:")))

#wap to find the square of a no if it is even 
# result=lambda num: print(num**2) if num%2 ==0 else None
# result(12)
# (lambda num: print(num**2) if num%2 ==0 else None)(int(input()))

#wap to find the square of a no if it is even otherwise print its cube
(lambda num: print(num**2) if num%2 ==0 else print(num**3 ))(int(input("Enter a no: ")))


#WAP to check if a no is postive or negative or zero 
result=lambda num: print("POS") if num>0 else print("NEG") if num<0 else print("Zero")
result(int(input()))
