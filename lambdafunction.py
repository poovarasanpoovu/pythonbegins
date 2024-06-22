

print("Lambda\n--------")

#lambda function is a set pass more argument but get only one experience

x = lambda a: a+10
print("Total value is: ",x(10))

#pass to two arguments

x = lambda a,b: a+b
print("Total (A+B)value is: ",x(10,20))

#Lambda using in side the function

def something(a):
    return lambda b: a+b

added = something(20)
print("Added value using fuction: ",added(20))