print("Factorial\n-----------")

num = 2
fac = 1
if num<0:
    print("Factorial does not exist from negative numbers")
elif num==0:
    print("Please enter more than 1 value")
else:
    for i in range(1,num+1):
        fac = fac * i
    print(num, "Factorial number is: ",fac)

print("Using def function factorial\n------------------------------")

print("Factorial\n-----------")

def fact(num):
 fac = 1
 if num<0:
    print("Factorial does not exist from negative numbers")
 elif num==0:
    print("Please enter more than 1 value")
 else:
    for i in range(1,num+1):
        fac = fac * i
    print(num, "Factorial number is: ",fac)

fact(4)
