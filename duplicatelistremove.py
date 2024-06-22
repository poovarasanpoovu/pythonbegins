
def list_dupremove():

   print("List Duplicate Remove using Map and List comprehension Function\n--------------------------------------")

   #Getting mulpiple input from user , at that time remove duplicate with print values

   multiple_entry = list(map(int,input("Enter the Item's : ").split())) # Map function using multiple inputs from user
   result=[]
   [result.append(i) for i in multiple_entry if i not in result]# List comprehension using check then not added duplicate item
   print("Final Output: ",result)

list_dupremove()

def find_dupitem():
  print("getting repeated values from the list".title().center(50, "*"))
  numbers = [1, 2, 4, 7, 5, 8, 3, 5, 6, 5, 3, 6, 6, 7, 6, 7, 8, 8, 7]  # use this one (or) below map x
  original = []
  duplicate = []
  try:

    x = list(map(int,input("Enter List Item's: ").split()))

    for i in x:

      if i not in original : #item not in list then add list in duplicate ignored
        original.append(i)
        original.sort()

      else: #Dup item comes in this else statement then print duplicate item
        if i not in duplicate: #Dup list already present means ignore the item
          duplicate.append(i)

  except ValueError:
      print("'Allowed Numeric Values Only!!!'")

  else:
      print("Duplicate Item in List is : ", duplicate)
      print("Original Item in List with Sorted : ", original)

  finally:
      print("Welcome's You!!!")

find_dupitem()







