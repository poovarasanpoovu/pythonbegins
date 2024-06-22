

#variable assign to one variable one value, two variable two values(using Comma), two variable one value(Using Equal To(=))
# if assign one variable multiple value but python is convert tuple(ex: a = 1,2,3) out but is (1,2,3)
#variable declared format is int,,float,string,boolean

value = 20.12
value = "Python"
value = False
print(value)
#boolean value using condition type
if value:print("Not Empty") #if variable value is  True not empty and false is empty
else: print("Empty")

a = 10
b,c = 20,20
d=e=10
f = 1,2,3

print(a) #10
print(b,c) #10 20
print(d,e) # both value is 10
print(f) # (1,2,3) its tuple
print("-------------------")
print(b+c)
print("The addition value is: ",b+c) #if ussing + symbol error will appear reason + using its string joiner so we again covert typecasting. mostly use (comma)
print("-------------------")
#Using special sequence in print() method

print("Welcome \t \n \bpython")
#return Ture or false
print(a>b)#its false a=10 b= 20
print("-------------------")

#local Global-using function
a=10 #global
def something():
    a=11 #local
    print(a)
something()

print(a)
print("-------------------")
#global value access in local and change global inside the function
a=20
def usingglobal():
    global a #global keyword using call global variable
    print(a) #result is 20
    a = 30 #global variable changed the value in inside the function
    print(a)
usingglobal()
print(a)#after chnages made in inside funtion affected in function outside


