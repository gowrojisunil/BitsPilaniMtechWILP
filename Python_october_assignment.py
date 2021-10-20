#!/usr/bin/env python
# coding: utf-8

# # DSECLPFDS - Python Exercises for Practice (S1 to S3)

# 1. Given a number, find the sum of its digits. Take the number as
# an input from the user.

# In[1]:



# take input from the user
num = input("Please enter a number: ")

sum = 0

for digit in str(num): 
  sum += int(digit)
print("Sum of its digits of the entered number is ", sum)


# 2. Given a number, check whether the given number is an
# Armstrong number or not. A positive integer is called an
# Armstrong number of order n if:
# abcd... = an
#  + bn + cn
#  + dn
#  + ...
# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
# 153 is an Armstrong number of order 3.
# Inputs from the user will be number and order n

# In[2]:


# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num is sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# 3. Given a string, write a python function to check if it is
# palindrome or not. A string is said to be palindrome if the reverse
# of the string is the same as string. For example, “malayalam” is a
# palindrome, but “music” is not a palindrome.

# In[3]:


# take input from the user
word = input("Enter a word: ")

if (word == word[::-1]):
  print("You Entered word is palindrome")
else:
  print("Not palindrome")


# 4. Given an array which may contain duplicates, print all elements
# and their frequencies.

# In[4]:


# creating an empty list
arr = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    arr.append(ele) # adding the element
    array_len = len(arr)
print("Array is :",arr, " and its length is :", array_len)

 # Mark all array elements as not visited
visited = [False for i in range(array_len)]

# Traverse through array elements
# and count frequencies
for i in range(array_len):
         
# Skip this element if already  processed
    if (visited[i] == True):
        continue
 
  # Count frequency
    count = 1
    for j in range(i + 1, array_len, 1):
        if (arr[i] == arr[j]):
            visited[j] = True
            count += 1
         
    print(arr[i], count)


# 5. Given a number n, write a function to print all prime factors of
# n. For example, if the input number is 12, then output should be
# “2 2 3”.

# In[5]:


import math

# A function to print all prime factors of
# a given number n
def primeFactors(n):

    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n / 2
        
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):

        # while i divides n , print i and divide n
        while n % i== 0:
            print(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)

# Driver Program to test above function

n = int(input("Enter a number: "))
primeFactors(n)


# 6. Given two numbers n and r, find the value of nCr (binomial
# coefficient: nCr = (n!) / (r! * (n-r)!))

# In[9]:


def factorial(n):
    # Write a function to compute factorial
    product = 1
    for i in range(1, n+1): product *= i
    return product

def ncr(n, r):
    # Use the function above to compute the nCr value
    return factorial(n) / factorial(r) / factorial(n - r)

n = int(input("please enter n :"))
r = int(input("please enter r :"))


print(n, "C", r, " = ", ncr(n, r), sep = "")


# 7. Searching: Given a sorted array arr[] of n elements, write a
# function to search a given element x in arr[]. Do it using linear
# and binary search techniques.

# In[14]:


# Linear search

def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
# arr = ['t','u','t','o','r','i','a','l']

# creating an empty list
arr = []
 
# number of elements as input
n = int(input("Enter english of characters : "))
 
# iterating till the range
for i in range(0, n):
    ele = input()
 
    arr.append(ele) # adding the element
    array_len = len(arr)
    
print("Array is :",arr, " and its length is :", array_len)

x = input("Enter a character which need to be searched: ")
# x = 'a'
print("element found at index "+str(linearsearch(arr,x)))


# In[15]:


# Binary Search

# Python3 Program for recursive binary search.
 
# Returns index of x in arr if present, else -1
def binarySearch (arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
         
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
        # Element is not present in the array
        return -1
 
# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")


# 8. Input a text file (containing 1 or more paragraphs of English
# text) from the user, parse this file to display the frequency of
# occurrence of each word in this text file. Find the 3 most frequent
# words as well.

# In[16]:


count = 0;  
word = "";  
maxCount = 0;  
words = [];  
   
#Opens a any format file in read mode  
file = open("data.rtf", "r")  
      
#Gets each line till end of file is reached  
for line in file:  
    #Splits each line into words  
    string = line.lower().replace(',','').replace('.','').split(" ");  
    #Adding all words generated in previous step into words  
    for s in string:  
        words.append(s);  
   
#Determine the most repeated word in a file  
for i in range(0, len(words)):  
    count = 1;  
    #Count each word in the file and store it in variable count  
    for j in range(i+1, len(words)):  
        if(words[i] == words[j]):  
            count = count + 1;  
              
    #If maxCount is less than count then store value of count in maxCount  
    #and corresponding word to variable word  
    if(count > maxCount):  
        maxCount = count;  
        word = words[i];  
          
print("Most repeated word: " + word);  
file.close();  


# In[ ]:




