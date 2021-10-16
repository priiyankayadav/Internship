#!/usr/bin/env python
# coding: utf-8

# #                   PYTHON ASSIGNMENT

# 11.  Write a python program to find the factorial of a number.

# In[2]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# In[3]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# 12.  Write a python program to find whether a number is prime or composite.

# In[4]:


# taking input from user
number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")


# In[5]:


# taking input from user
number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")


# 13.  Write a python program to check whether a given string is palindrome or not.

# In[6]:


n = input("Enter the word and see if it is palindrome: ") #check palindrome
if n == n[::-1]:
    print("This word is palindrome")
else:
    print("This word is not palindrome")


# In[7]:


n = input("Enter the word and see if it is palindrome: ") #check palindrome
if n == n[::-1]:
    print("This word is palindrome")
else:
    print("This word is not palindrome")


# 14.  Write a Python program to get the third side of right-angled triangle from two sides.

# In[9]:


def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


# 15. Write a python program to print the frequency of each of the characters present in a given string.

# In[13]:


string = "picture perfect";  
freq = [None] * len(string);  
   
for i in range(0, len(string)):  
    freq[i] = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j]):  
            freq[i] = freq[i] + 1;  
              
            #Set string[j] to 0 to avoid printing visited character  
            string = string[ : j] + '0' + string[j+1 : ];  
              
#Displays the each character and their corresponding frequency  
print("Characters and their corresponding frequencies");  
for i in range(0, len(freq)):  
    if(string[i] != ' ' and string[i] != '0'):  
        print(string[i] + "-" + str(freq[i]));  

