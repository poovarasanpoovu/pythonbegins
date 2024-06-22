#collection values in singel varibale to use
#list,tuple,dictionaries,set

#all data-types allowed
#List = ordered,changeable,duplicate allows----> [0,1,2,3]-start with zeros indexing
#Tuple = ordered,unchangeable,duplicate allows
#Dict = orered,changeable,n oduplicate allows
#Set = un-ordered,un-changeable,no duplicate allows

print("Tuple Access\n-------------")
datas = ("Suresh",1,12.13,True)
print(type(datas))

#Finding using index values
print("The tuple: ",datas)
print("1st indexing value is :",datas[1])

#Tuple dont allow to change the value
#datas[1]=2 error will be accur
# So we can convert Tuple to List
new_datas = list(datas)
print("Now tuple to list convertion :",new_datas)

#Now modify the value in list-Anythin we can change the value using tuple to list and list to tuple
new_datas[1]=2
print("Modify value is: ",new_datas)
print("Modify value convert list to tuple: ",tuple(new_datas))

#2D tuple
name= ("John","Wick","petter",)
another_addded = (datas, name)
print("Two tuple: ",another_addded)
print("1st & 2nd value: ",another_addded[1][2])

#for loop useing in tuple
for i in datas:
    print(i, end = "-")

#while using in tuple
num=0
while num<=len(datas):
    num+=1
print("\ntuple values: ", datas)

#for loop using collecting the values

user_number = (1,2,3,4)
sum = 0
for i in user_number:
    sum = sum + i
print("The total value is: ",sum)

#For loop using added the two tuple values-But convert list

number = (1,2,3,4)
number1 = (5,6,7,8)
total_value = []

for i in range(0,len(number)):
    total_value.append(number[i] + number1[i])
print("Total two tuple values are: ",tuple(total_value))
