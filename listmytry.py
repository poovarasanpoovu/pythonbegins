
print("Getting 1'st value from each indexing".title().center(50,"*"),"\n")

numbers=[[1,2,3],[4,5,6],[7,8,9]]
result=[]

for i in numbers:
    result.append(i[0])
print("2D list each every item 1st value is: ",result)

print("Same result but using List comprehension:".center(50,"*"),"\n")

x = [i[0] for i in numbers]
print(f"Final Output of {numbers} : ",x)


print("Getting 1'st Value From Each Indexing To Be made by Addition".title().center(70,"*"),"\n")
#Each index 1st value to added with using loop statement
def operation_forlist():
    for i in range(0,len(numbers)):
         # Notes : If sum variable is mentioned before the "for in range(0,len(num)) statement getting result (12, (12+15)=27 ,(12+15+18)= 45) sum is added value
         # Sum variable stored once then loop run value will be added with stored value each iterator
        sum = 0
        get_index =[]
        for j in numbers:
            sum=sum+j[i]
            get_index.append(j[i])
        print(f"Item index[{i}] & Value is [{get_index}] Added Total :",sum)

#operation_forlist()

print("Getting each index total Value From the list".title().center(70,"*"),"\n")
#Getting each index total item will be added
def index_addedtotal():

    for i in range(0, len(numbers)):
        sum = 0
        index= []
        for j in numbers[i]:
            sum = sum + j
            index.append(j)
        print(f"Index[{i}] & value is {index} Total is: ",sum)
#index_addedtotal()













