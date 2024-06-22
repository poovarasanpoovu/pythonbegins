import time

start_time = time.time()

for i in range(1,20):
    for j in range(1,i+1):
      print("*",end = "")
    print("")

end_time = time.time()
print("The program execution time is : ",(start_time-end_time)* 10**3,"ms")