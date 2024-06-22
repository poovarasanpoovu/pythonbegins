print("File Handling\n-------------")

with open("newfile")  as new: #import file using with keyword and open method, as keying word instead of newfile
  print(new.read())

#write in file

added = "We write coding with file accessing"
with open("newfile",'w') as a: # w means write if using write already content deleted and new content only present in file
   a.write(added)
added1 = "  append "
with open("newfile",'a') as b: #a means append
   b.write(added1)

#creating a new file

with open("new1","x") as a:
    a.write("New file has been created successfully")

#Deleted File

import os # import os function

os.remove("new1")
if True:
    print("Successfully Removed File From Drive")

os.unlink("newfile") #this method also delete the file
if True:
    print("Successfully Removed File From Drive")

#Using(r+,w+,a+)
# r+ --> Read & Write at a time
# w+ --> Write & Read at a time
# a+ --> Append & Read at a time

#File Renaming

import os
a.rename("new1","new2")

print("--------------------------------------------------------------------")

print("file handling program!!!".title().center(50,"*"))

def create_file(file_name):
    try:
        with open(file_name,"w") as f:
            f.write("We have created new text file!!!")
        print(f"Create Mode : File {file_name} successfully created!!!")

    except IOError:
        print("File not created".title(),file_name)


def read_file(file_name):

    try:
        with open(file_name,"r") as f:
           print(f"Read Mode : {f.read()}")

    except IOError:
        print("File unable to read ".title(),file_name)

def append_file(file_name):

    try:
        with open(file_name,"a") as f:
            f.write("\n This file created from pycharm IDE!!!")
        print(f"Append Mode : {file_name} successfully appended!!!")

    except IOError:
        print("File not Appended".title(),file_name)

def rename_file(file_name,new_filename):

    try:
       os.rename(file_name,new_filename)
       print(f"Rename Mode : File old name is : {file_name} to New name for : {new_filename}")
    except IOError:
        print("Rename unsuccessful changed!!!".title())


def deleted_file(file_name):
    try:
        os.remove(file_name)
        print(f"Delete Mode : File {file_name} deleted successfully!!!")
    except IOError:
        print("Deleted failed!!!".title())


file_name="testing.txt"
rename_files="sample.txt"

create_file(file_name)
read_file(file_name)
append_file(file_name)
rename_file(file_name,rename_files)
deleted_file(rename_files)

