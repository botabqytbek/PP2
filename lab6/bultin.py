import math
import time

#1 Write a Python program with builtin function to multiply all the numbers in a list
numb = list(map(int, input().split()))
print(math.prod(numb))

#2 Write a Python program with builtin
#function that accepts a string and calculate the number of upper case letters and lower case letters
s = input()
u=0
l=0
for char in s:
    if char.isupper():
        u+=1
for char in s:
    if char.islower():
        l+=1
print("uppers: ",u)
print("lowers: ",l)

#3 Write a Python program with builtin function that checks whether a passed string is palindrome or not.
s = input()
def pal(s):
    for i in s:
        d = ''.join(i.lower())
    return d == d[::-1]
if pal(s):
    print("palindrom")
else:
   print("not palindrom") 

#4 Write a Python program that invoke square root function after specific milliseconds
msec = int(input())
a = int(input())
print(f"Square root of {a} after {msec} milliseconds is {math.sqrt(a)}")

#5 Write a Python program with builtin function that returns True if all elements of the tuple are true.
t1 = (True, True, True)
t2 = (True, False, False)

if all(t1):
    print("t1 - True")
else:
    print("t1 - False")

if all(t2):
    print("t2 - True")
else:
    print("t2 - False")
