
#list append similar generators
def something(num):
      new = []
      for i in range(1,num+1):
         new.append(i*i)
      return new
print(something(10))

#Generators using below example using yield keyword
def somenew(num):
       for i in range(1,num+1):
             yield i*i


new =somenew(5)
for i in new:
    print(i , end = " ,")
