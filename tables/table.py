#to create the table with while condition
number=int(input("enter number: "))
counter=1
while counter<=10:
    multiplication=number*counter
    result=str(number)+" X "+str(counter)+" = "+str(multiplication)
    print(result)
    counter=counter+1

#to create the table with for loop condition
num=int(input("enter num:"))
for i in range(1,num+1):
    multiplication=num*i
    result=str(num)+" X "+str(i)+" = "+str(multiplication)
    print(result)