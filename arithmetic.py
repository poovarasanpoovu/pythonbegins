

a =''
b = ''
name =''
choice=''
while choice!="5":
   a = int(input("Enter A value: "))
   b = int(input("Enter B value: "))
   choice = int(input("Please Enter the choice(1/2/3/4): "))
   if choice == 1:
    print("Addition value is:",a+b)
   elif choice == 2:
    print("Substraction value is:", a - b)
   elif choice == 3:
    print("Multiplication value is:", a * b)
   elif choice == 4:
    print("Division value is:", a / b)
   else:
       print("\t Kindly enter choice number between 0 to 4")