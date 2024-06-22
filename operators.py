
print("if,elif,else - 7 Operators Using\n-------------------------------")

#using operator to check condition-Arithmetic,assignment,comparison,logical,identify,membership,bitwise

print("Arithmetic Operators:")
# +,-,*./,%,//,**
a = 2
b = 4
print(a+b) #using another operators

print("Assignment Operators:")
# +=,-=,*=./=,%=,//=,**=
a**=5
print(a)

print("comparision Operators:")
#=,>,<,>=,<=,!=
a = 3
b = 3
#print("A is grater than B")if a>b else print("A is less than B")
print("A is grater than B")if a>b else print("A & B are Equal")if a==b else print("A is less than B")
if a!=10:
    print("True")
else:
    print("False")

print("logical Operators:")
# and , or ,not
a = 15
b = 10
c = 30
# and keyword using both condition is true
# or keyword using either one condition is true
# not  keyword using both condition is true result false
if a>b and a<c:print("A is greater than B and A is less than C") #10>9 and 10<20
else: print("A is less than B or  A is greater than C")

if a>b or a<c:print("A is greater than B or A is less than C") #10>9 or 10<20
else: print("A is greater than B  and  A is less than C")

if not(a>b and a<c):
    print("Both equal but result shows false")
else:
    print("One condition is false")

