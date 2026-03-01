#two sum
def Twosum(list1,target):
    length=len(list1)
    for i in range(0,length):
        for j in range(i+1,length):
            if list1[i]+list1[j]==target:
                return ((i,j))

val=Twosum([1,2,5],4)
print(val)

#Unique Transactions
transactions=[35353,23232,576767,3333,3333,3333]
s=set(transactions)
print(s)