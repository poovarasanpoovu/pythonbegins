

print("f-String\n--------")

#its similar to string format but more faster than format() method
name = "Python"
print(f"welcome {name}")

value = 10
value1 = 20
print(f"The first value is  {value} and second value is {value1}")
print(f"Two numbers added : {value+value1}")


print(f"The  {name:>10}object oriented programming language")
print(f"The  {name:<10}object oriented programming language")
print(f"The  {name:^10}object oriented programming language")

number = 1000000
number1 =10
number2 =10.123
number3 = 0.12

print(f"Using comma split value: {number:,}")
print(f"Getting binary value: {number1:b}")
print(f"Getting decimel value: {number2:.2f}")
print(f"getting percentage value : {number3:%}")
