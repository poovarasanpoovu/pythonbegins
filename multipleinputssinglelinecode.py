print("Multiple Input from user in a single line command".title(),"\n-----------------------------")

print("1.split() Method")

'''a,b= input("Enter the value :").split()
print("One input method getting two values: ",a,b)

a,b,c= input("Enter the value :").split()
print("One input method getting three values: ",a,b,c)

a= input("Enter the value :").split()
print("One input method getting multiple values: ",a)#its run time converted as list


print("2.Map() & Split() Function\n---------------------")

x,y=map(int,input("Enter the value :").split())
print("Tow values getting:",x,y)

x=map(int,input("Enter the values: ").split())
print(x) # multiple time using for loop or typecasting as list
for y in x:
   print(y,end="")
x=list(map(int,input("Enter the values: ").split()))
print("List value: ",x)

print("3.List comprehension\n-------------------")

x= [int(i) for i in input("enter the value : ").split()]
print("List value are:",x)'''

print("4.For loop\n--------")

for i in input("enter the value: ".title()):print(i,end= "")