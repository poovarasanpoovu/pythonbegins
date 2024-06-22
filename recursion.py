
print("Recursion\n---------")

def fact(num):
    if num == 0:
        return 1
    return num*fact(num-1)
#Process of recursion
''' 5*4=5*24=120 F5 
     4*3=4*6 F4
     3*2=3*2 F3
     2*1=2*1 F2
     1*1=1 F1'''

value = int(input("Please enter value : "))
print("The factorial number is : ",fact(value))