#collection values in singel varibale to use
#list,tuple,dictionaries,set

#all data-types allowed
#List = ordered,changeable,duplicate allows----> [0,1,2,3]-start with zeros indexing
#Tuple = ordered,unchangeable,duplicate allows
#Dict = orered,changeable,n oduplicate allows
#Set = un-ordered,un-changeable,no duplicate allows

print("List Access\n-------------")
datas = ["Suresh",1,12.13,True]
print(type(datas))

#Finding using index values
print("2nd value in list: ",datas[2])
print("Reversed in list: ",datas[::-1])
print("start to 2nd slicing in list: ",datas[:2])
print("start to end skipping 2 values  in list: ",datas[::2])
print("Negative values in list: ",datas[-1])
datas[2]="Poovarasan"
print("Insert but changed the position in list: ",datas)

#insert another way using methods insert
datas.insert(2,12.13)
print(datas)

#append using last added the value
datas.append("Red")
print(datas)

#remove in list values
datas.remove("Poovarasan")
print(datas)

#modifying
datas[1]=2
print(datas)

#del values in list
del datas[4]
print(datas)

#Copy the list
new = datas
print("The copy the listing in new: ",new)

#if changed in new list affect in datas list also
new.append("Poovarasan")
print("The Poovarasan added in new but also affect in datas: ",datas)

#Copy the list but don't affect original varibale
new = datas[:]
print(new)

#if changed values in new variable not affect in original datats
new.append("added new value in new V")
print("New variable: ",new)
print("datas variable: ",datas)

#variable to pass in list-2D list
name = ["John","petter","wick","ban"]
age = [30,20,50,35]
country = ["America", "japan","london","paris"]
details = [name,age,country]
print(details)
print("Zero list & 1st value getting: ", details[0][1])

#append list in list
details[0].append(["a","b","c","d"])
print("Add list in list :" ,details)
print("getting from Zero list and 4th list in 2nd value is :",details[0][4][1])

#if we change in name ,age, country variable affect in details variable also
name.remove("ban")
print("name variable remove ban name in list and affect in details varibale :", details)

#using some method like as title ,reverse,remove ,replace,insert,append,del keyword,pop
#pop() method can use delete the last value and return the value also

number = [1,2,3,4,5]
deleted_value = number.pop()
print("The last value 5 is deleted :",number)
print("Deleted value is :",deleted_value)


print("1st item each iterator\n-------------------")

name=["Tom","Jerry","petter"]
color= ["red","black","white"]

result=[]


for i in range(0,len(name)):
    result.append([name[i],color[i]])
print("The Iterator each one :",result)


























