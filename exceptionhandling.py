print("Exception Handling\n___________")

#Errro will find before run the code and write manually error msg


try : #error block
    num = int(input("Enter tha value: "))
    num1 = int(input("Enter tha value: "))
    result = num / num1

except ZeroDivisionError: #its specified error msg
    print("Don't enter zero division")
except ValueError:#its specified error msg
    print("Don't enter alphbetics")
except Exception: #except keyword using user create error msg and exception is all error example zerodivisionerror
    print("Please enter correct value")
else: #can use else statement also final out
    print(result)
finally:#its print always error or looks good coding
    print("Thanks")

