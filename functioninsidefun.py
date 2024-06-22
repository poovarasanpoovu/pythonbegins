

def something(num,num1):
        sum = []
        for i in range(0,len(num)):
            sum.append(num[i]*num1[i])
        print(f"{num} (*) {num1} =",sum)
        def maximum_value():
            print("Max value in the list: ",max(sum))
        maximum_value()
        def append_list():
            sum.append(num+num1)
            print("Append list items : ",sum)
        append_list()



numbers = [1,2,3,4]
another_number = [5,6,7,8]
something(numbers,another_number)
