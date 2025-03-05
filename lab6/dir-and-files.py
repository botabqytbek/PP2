import sys
import os

#1 Write a Python program to list only directories, files and all directories, files in a specified path.
dir = []
fil = []
path = input()
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        dir.append(i)
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        fil.append(i)
print(dir)
print(fil)


#2 Write a Python program to check for access to a specified path. 
#Test the existence, readability, writability and executability of the specified path
path = input()
access = {
        'exist': os.path.exists(path),
        'read': os.access(path, os.R_OK),
        'write': os.access(path, os.W_OK),
        'exec': os.access(path, os.X_OK)
    }

if access['exist'] and access['read'] and access['write'] and access['exec']:
    print("Full access")

#3 Write a Python program to test whether a given path exists or not.
#If the path exist find the filename and directory portion of the given path.
    path = input()
if os.path.exists(path):
    print(os.path.basename(path), os.path.dirname(path))
    
#4 Write a Python program to count the number of lines in a text file.
    l =0
with open('text.txt', 'r') as file:
    for line in file:
        l += 1    
print(l)

#5 Write a Python program to write a list to a file.
l = list(map(int, input().split()))
with open('text.txt', 'w') as file:
    for i in l:
        file.write(str(i)+ "\n")

#6 Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in alpha:
    f = i + ".txt"
    with open(f, 'w') as file:
        file.write("hello")

#7 Write a Python program to copy the contents of a file to another file
with open("A.txt", 'r') as src, open("text.txt", 'w') as dest:
    dest.write(src.read())

#8 Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
path = input()
access = {
        'exist': os.path.exists(path),
        'read': os.access(path, os.R_OK),
        'write': os.access(path, os.W_OK),
        'exec': os.access(path, os.X_OK)
    }

if access['exist'] and access['read'] and access['write'] and access['exec']:
    print("Full access")
os.remove(path)
