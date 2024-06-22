value = ""
added = []
while value!="t":
    value= input("Enter the list: ")
    if value=="t":
        break
    added.append(value)
print("Final list is: ",added,"\nTotal items in list is: ",len(added))
print("Welcome Items changes floor")
changes = input("If any changes made in list (Y/N): ")
modify=''

if changes.upper()=="Y":
 while modify != "exit":
    print("Type of changes\n1.insert\n2.Added\n3.Replace\n4.Delete\n5.Reverse\n6.Sorted\n7.Getting Items :")
    modify = input("Enter the the number: ")
    if modify=="1":
        print("Insert List\n-------------")
        insert = int(input("Insert position : "))
        insert1 = input("Insert item : ")
        added.insert(insert,insert1)
        print("Inserted & List Item: ",added)
    elif modify=="2":
        print("Added List\n-----------")
        add = input("Enter the item :")
        added.append(add)
        print("New Item in List: ",added)
    elif modify=="3":
        print("Replace List\n-------------")
        position = int(input("Enter the position: "))
        remove1 = input("enter the item name: ")
        added[position]=remove1
        print("Replaced & List Item: ",added)
    elif modify=="4":
        print("Deleted Item\n------------")
        deleted = int(input("Enter the position:  "))
        del added[deleted]
        print("Deleted & Balance List Items :",added)
    elif modify=="5":
        print("Reversed Item\n------------")
        added.reverse()
        print("Reversed Items :",added)
    elif modify=="6":
        print("Sorted Item\n-------------")
        added.sort()
        print("Sorted Items: ",added)
    elif modify=="7":
        print("Getting Item\n-------------")
        getting = int(input("Enter Index value: "))
        print("The",getting,"th Index List Item is : ",added[getting])

 print("Thanks For Using!!!")

else:
    print("Your final Output of the list is: ",added)


