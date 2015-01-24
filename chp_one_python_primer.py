
# coding: utf-8

### Exercise 1 : Python Primer

# 1.1) Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

# In[18]:

def is_multiple(n,m):
    """ Checks if n is a factor of m where n <= m """
    try:
        if m%n == 0:
            print "Yes! {0} is a factor of {1}".format(n,m)
        else:
            print("\n Nope! {0} is NOT a factor of {1}".format(n,m))
    except Exception as excpt:
        print "Error!", excpt
    return
        

is_multiple(15,3)


# 1.2) Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. <em>However, your function
# cannot use the multiplication, modulo, or division operators.</em>

# In[30]:

invalue = input("Enter a value to check > ")

print("\nBam! %d is Even!\n"%invalue if (-1)**invalue == 1 else "No way! %d is not even.\n" %invalue)

print("Yeah, it's Even number!\n" if invalue%2 == 0 else "No way! It's not.\n")


# 1.3) Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. <em>Do not use the built-in functions min or
# max in implementing your solution.</em>

# In[4]:

def minimaxi():
    """ Returns the minimum and maximum from the list """
    
    try:
        data = input("Enter a list of any input > ")
        smally = biggy = data[0]
        for n in data:
            if n >= biggy:
                biggy = n
            elif n <= smally:
                smally = n
            else: pass
        print (smally,biggy)
    except Exception as excpt:
        print "\nBad input found. ", excpt
    return
        
minimaxi()


# 1.4) Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

# In[21]:

def sumsquare():
    ''' Returns sum of square of all positive numbers less than n '''
    sqrsum = 0
    try:
        inpdata = input("Enter a number > ")
        if not isinstance(inpdata,int):
            print("input value must be integer")
        elif inpdata <= 2:
            print ("Sum of square is 1")
        else:
            for k in range(inpdata):
                sqrsum += k**2
            print("\n\nSum of square of element < %d is %d " % (inpdata,sqrsum))
    except Exception as excpt:
        print "Yikees! ", excpt
    return



sumsquare()


# 1.5) Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.

# In[24]:

sum([k**2 for k in range(5)])


# 1.11) Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

# In[28]:

[2**k for k in range(input("Enter a number > "))]


# In[46]:

import random

print random.choice(range(5))
print random.randrange(1,5)


# 1.19) Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

# In[53]:

import string

alphalower = list(string.ascii_lowercase)

print alphalower


# 1.29 Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once. (Incomplete)

# In[60]:

import random

alplist = ['c','a','t','d','o','g']

random.shuffle(alplist)

alplist


# In[ ]:



