#collection values in singel varibale to use
#list,tuple,dictionaries,set

#all data-types allowed
#List = ordered,changeable,duplicate allows----> [0,1,2,3]-start with zeros indexing
#Tuple = ordered,unchangeable,duplicate allows
#Dict = orered,changeable,n oduplicate allows
#Set = un-ordered,un-changeable,no duplicate allows

print("Set Access\n-------------")
datas = {"Suresh",1,12.13,True}
print(type(datas))

#Duplicate not allow

datas = {"Suresh",1,12.13,True}#true is 1 and false is 0
print("True not appear: ",datas)

datas = {"Suresh",1,12.13,1,"poovarasan",12.13,-1,0,False}
print(datas)

#another way to declared set
datas_new = set((12,3,44,12,"suresh",True))
print("another way to declared set: ",datas_new)

#for loop
added_value = set((1,2,3,4))
sum = 0
for i in added_value:
    sum = sum + i
print("Total value of set :",sum)

#while loop
num=1
sum = 0
while num<=(len(added_value)):
    num+=1
print("The value is: ",added_value)

#Set into List

list_update = list(added_value)
print("List :",list_update)

#if changes affect in set

list_update.append("5")
print(list_update)#list only update 5
print(added_value)#not appear in 5
print(set(list_update))#now convert 5 appear in set

