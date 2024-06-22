
print("Getting 1st value in each item\n-----------------------------------------")
color= ["red","blue","white","orange"]

first_item = []

for i in color: first_item.append(i[0].title())
print("Final Output with Caps: ",first_item)

print("Getting 1st three item\n-------------------------")

first_three_item = []

for i in color: first_three_item.append(i[:3].title())
print("Final Output with Caps: ",first_three_item)