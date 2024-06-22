

print("Finding Prime Numbers\n---------------------")
num = 0
if num>1:
        for i in range(2,int((num/2))):
            if num%i == 0:
                print("Its not prime number is: ",num)
                break
        else:
            print("Its prime number is: ",num)
else:
         print("Please enter the value is more than 1 !!!")