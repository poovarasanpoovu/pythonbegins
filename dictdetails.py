#collection values in singel varibale to use
#list,tuple,dictionaries,set

#all data-types allowed
#List = ordered,changeable,duplicate allows----> [0,1,2,3]-start with zeros indexing
#Tuple = ordered,unchangeable,duplicate allows
#Dict = orered,changeable,n oduplicate allows
#Set = un-ordered,un-changeable,no duplicate allows

print("Dict Access\n-------------")
datas = {"name" : "john", "age" : 25, "country" : "London"}
print(type(datas))

#Dict is key and value if we add,change anything using key
print("The 1st value in dict: ",datas["age"])

print("Keys in dict: ",datas.keys())
print("Value in dict: ",datas.values())

datas["name"]="peter" #changes
print("Name key change the value  in dict: ",datas)

datas["color"]="red" #added
print("Color key added in dict: ",datas)

#del datas["color"] #delete
#print("Deleted the color key in dict: ",datas)

getting = datas.pop("color")
print("Deleted the color key in dict: ",datas)
print("Deleted value is :",getting)

new_datas = {"name": "john", "age": 28, "country": "america"}

datas = [datas,new_datas]
print("Two dict joined: ",datas)

#getting value
print("1st dict name value: ",datas[0]["name"])

#for loop using split key and values

getting_value = {"name": "john", "age": 28, "country": "america"}
for i in range(0,1):
    print(getting_value.keys())
    print(getting_value.values())

#list convert
list_convert = datas
print("list: ",list_convert)
print(type(list_convert))

for i in list_convert:
    print(i.values())

#if we added one key more values
getting_value["country"]=["london","paris","india"]
print(getting_value)

#Dict mentioned this ways also

user_input = dict(name = "suresh", age = 25, country = "india")
print("Dict keyword suing: ",user_input)

#duplicate not allowed

user_input = {"name": "suresh", "age" : 25, "country" : "india","age" : 26} #last key value is appeared in output
print(user_input)