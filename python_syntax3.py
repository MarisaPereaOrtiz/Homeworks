# -*- coding: utf-8 -*-
"""Copy of Python Syntax 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dbxkbtBp8KCrEX6yc_927c8QENMy-6Vm

# Intro to Python Syntax, Part 3
## Code and Data Assignment

## Python as an Ecosystem of Functions

There are millions of functions that can be used in Python.  To access them, you first have to **import** their **packages/modules**.  Then you can specify the functions inside the packages using the following syntax:

```python
import package
output = package.function(input)
```

Sometimes, packages have **subpackages** that contain functions, too:

```python
output = package.subpackage.function(input)
```

If you only need one subpackage in a function, you can make your lines shorter by importing the subpackage directly:

```python
from package import subpackage
output = subpackage.function(input)
```

To get a list of functions in a package, try using the **dir()** function.  To learn what the function does, try the **help()** function.

```python
import math
dir(math)
help(math.sqrt)
```

Let's try out the built-in **math** and **statistics** packages to do some calculating!

What is the mean of all the integers from 1 to 6?
"""

import statistics as stat
a_list = [1, 2, 3, 4, 5, 6]
stat.mean(a_list)

"""What is the standard deviation of the integers from 1 to 6?"""

stat.stdev(a_list)

"""What is the square root of 72?"""

stat.sqrt(72)

"""What is pi?"""

import math
pi = math.pi
print(pi)

"""What how many radians are in 360 degrees?"""

math.radians(360)

"""Can you find a package that might have functions for random numbers?  Use it to generate a couple random numbers!"""

import random

for i in range(3):
    random.randint(i+1,10)

"""Look for names of some more built-in packages online!  Try importing them here."""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)

plt.plot(x, y)
plt.xlim(-0.1, 10)
plt.ylim(-1, 1)
plt.show()

"""## Python as State Machine

Python can save all of its **objects** to your computer's internal memory by **assigning** a a **name** to it.  This is like giving the object a tag that can be referenced later, and it has many subtleties that we'll be exploring throughout the course.  Here's the syntax:

```
name = data
```

For example:

```python
x = 3
nick = 100
j_people = ["John", "Jeff", "Judy", "Jenny"]
x2 = 4
```

While it looks like a normal math expression, this is, in reality, a **statement**; it changes the state of the program.  Let's explore it here:

#### Exercises

What should **x** equal?
```python
x = 3
x = 4
```
"""

x = 3
x = 4
print(x)

"""```python
x = 3
x = x + 1
x = x + 1
x = x + 1
```
"""

x = 3
x = x + 1
x = x + 1
x = x + 1
print(x)

"""```python
x = 3
x += 1
x += 1
x += 1
```
"""

x = 3
x += 1
x += 1
x += 1
print(x)

"""```python
x = "Nick"
x = 0
```
"""

x = 'Nick'
x = 0
print(x)

"""```python
max = sum
x = max([1, 2, 3])
```
"""

max = sum
x = max([1, 2, 3])
print(x)

"""```python
max = sum
x = sum([1, 2, 3])
```
"""

max = sum
x = sum([1, 2, 3])
print(x)

"""```python
x = [1, 2, 3]
x[1] = 4
```
"""

x = [1, 2, 3]
x[1] = 4
print(x)

"""```python
x = [1, 2, 3]
x[-1] = 4
```
"""

x = [1, 2, 3]
x[-1] = 4
print(x)

"""```python
x = [1, 2, 3]
x[0] = 4
```
"""

x = [1, 2, 3]
x[0] = 4
print(x)

"""```python
x = [1, 2, 3]
x = x[1]
x *= 2
```
"""

x = [1, 2, 3]
x = x[1]
x *= 2
print(x)

"""### Mapping Collections: Transforming Each Element of a Collection

Often, you want to do something to the data inside your collection--double it, increase it, compute some metric, etc.  
At the end, you still have the same *number* of elements, but the values themselves have changed.  
We will be looking at lots of ways to accomplish this in  Python, but first we're going to use a **for-loop** in a format called a **comprehension**.

Comprehensions produce a new collection containing new values *"for each"* value *in* the original collection.  They look like this:

```python
>>> data = [1, 2, 3]
>>> list(x * 2 for x in data)
[1, 4, 9]
```

The code above does the same as the following:
```python
>>> data = [1, 2, 3]
>>> [data[0] * 2, data[1] * 2, data[2] * 2]
[1, 4, 9]
```

Another example:

```python
>>> data = [1, 2, 3]
>>> tuple(math.sqrt(value) + 2 for value in data)
(3.0, 3.414, 3.732)
```

```python
>>> data = [1, 2, 3]
>>> (math.sqrt(data[0]) + 2, math.sqrt(data[1]) + 2, math.sqrt(data[2]) + 2)
(3.0, 3.414, 3.732)
```

Notice that the variable **x** and **value** are created without using the assignment operator! You can name this anything you want, and it is created anew for each individual element of the collection.

For lists, Python has a shortcut (called a **list comprehension**):

```python
>>> data = [1, 2, 3]
>>> [x * 2 for x in data]
[1, 4, 9]
```

There is also one for dict (**"dict comprehensions"**), but not for any other type.  See below:

```python
>>> data = [1, 2, 3]
>>> {x: x * 2 for x in data}
{1: 1, 2: 4, 3: 9}
```

**Exercises**: Transform each value in the given collection into the requested collection type using the requested transformation

Example: A tuple of each value in "data", with each value increased by 3
```python
>>> data = [10, 20, 30]
>>> tuple(x + 3 for x in data)
(13, 23, 33)
```

1. Make a list that adds 1 to each value in "data":
"""

data = [1, 2, 3]
[x + 1 for x in data]

"""2. Make a tuple that calculates the absolute value of each element in "data", using the built-in abs() function:"""

data = (-2, -1, 0, 1, 2)
tuple(abs(x) for x in data)

"""2b. Make a list of the cosines of each value in "data":"""

import math
data = (-2, -1, 0, 1, 2, 3)
[math.cos(x) for x in data]

"""2c. Round all these numbers to the nearest integer (use the "round()" function):"""

data = [1.2, 1.5, 0.7, -2.1]
[round(x) for x in data]

"""3. Make a list of all the first letters of each name in the list:"""

data = ["John", "Harry", "Moe", "Luke"]
[x[0] for x in data]

"""4. Make a tuple of the lengths of each name:"""

data = ["John", "Harry", "Moe", "Luke"]
tuple(len(x) for x in data)

"""5. Make a dictionary that maps all the words in the list to their length:"""

data = ["John", "Harry", "Moe", "Luke"]
{x : len(x) for x in data}

"""6. Make a set of all the word lengths in the tuple:"""

data = ("John", "Harry", "Moe", "Luke")
set(len(x) for x in data)

"""### Filtering Collections

What if you only want to include *some* values in a collection?  With the **if** statement and a **logical expression**, you can do it in a comprehension!  For example:

```python
>>> data = [1, 2, 3, 4]
>>> [x for x in data if x > 2]
[3, 4]
```

This can be combined with various transformations as well!

```python
>>> data = ["John", "Harry", "Moe", "Luke"]
>>> [x[0] for x in data if len(x) < 5]
["J", "M", "L"]
```

**Exercises**:

Get All positive values in the following list:
"""

data = [-6, 3, -1, 10, -5, 0]
[x for x in data if x >= 0]

"""Make a tuple of all names that start with the letter "L":"""

data = ("John", "Harry", "Moe", "Luke")
tuple(x for x in data if x[0] == 'L')

"""Make a list of all names that have more than 3 letters in the name:"""

data = ("John", "Harry", "Moe", "Luke")
[x for x in data if len(x) > 3]

"""Make a list of the last letter of all names that have more than 3 letters in the name:"""

data = ("John", "Harry", "Moe", "Luke")
[x[-1] for x in data if len(x) > 3]

"""Make a list of all values who have positive cosines:"""

import math
data = [1, 2, 3, 4, 5, 6, 7]
[x for x in data if math.cos(x) >= 0]

"""Make a dictionary, mapping each name to its length, but only if the sine of its length is positive:"""

import math
data = ["John", "Harry", "Moe", "Luke"]
{x : len(x) for x in data if math.cos(len(x)) >= 0}

"""### Combining Them: Filtering, Transforming, and Aggregating

Okay, let's combine everything together into a single step!  To get the minimum value of the squares of all values less than 0 in the following list:

```python
>>> data = [-5, -3, 1, 2, 3]
>>> min(x ** 2 for x in data if x < 0)
9
```

Let's try it out!

**Exercises**:

The sum of all squares for all values in the dataset [1, 7, 3, 4, 9] greater than 4.
"""

data = [1, 7, 3, 4, 9]
sum(x**2 for x in data if x > 4)

"""The minimum length of all names in the list who has at least 4 unique letters in their name: ["Bobby", "Cindy", "Anna", "Joshua", "Alan", "Hannah", "Jeffrey"]"""

data = ["Bobby", "Cindy", "Anna", "Joshua", "Alan", "Hannah", "Jeffrey"]

min(len(x) for x in data if len(set(x.lower())) > 4)

"""The total length of all the names in the list that starts with an "R": ["Joey", "Monica", "Chandler", "Rachel", "Ross", "Phoebe"]"""

data = ["Joey", "Monica", "Chandler", "Rachel", "Ross", "Phoebe"]
sum(len(x) for x in data if x[0] == 'R')



"""### Chaining Them: Repeatedly Filtering and Transforming before Aggregating
Often, data analysis pipelines require multiple repeated transforms and filters before the analysis is complete.  This can get quite unwieldy, to say the least.  For example:
"""

tuple(x for x in (x ** 2 for x in (len(x) for x in (x for x in ["Joey", "Monica", "Chandler", "Rachel", "Ross", "Phoebe"]) if x[0] == 'R') if x < 10) if x < 36)

"""You could split this into multiple lines, but it doesn't always help keep it readable.  For example:"""

tuple \
(x for x in 
(x ** 2 for x in 
(len(x) for x in
(x for x in 
["Joey", "Monica", "Chandler", "Rachel", "Ross", "Phoebe"])
if x[0] == 'R')
if x < 10) 
if x < 36)

"""The simplest way is to just split it into multiple steps:"""

friends = ["Joey", "Monica", "Chandler", "Rachel", "Ross", "Phoebe"]
friends = [len(x) for x in friends if x[0] == 'R']
friends = [x ** 2 for x in friends if x < 10]
tuple(x for x in friends if x < 36)

"""This is a little better, but it can be a lot simpler.  We will be looking at many ways to make it easier for us to transform and filter data in later units.

## Review: Class Discussion

  1. Python has a lot of symbols in its syntax.  What are they, and what are they used for?
  2. What are functions?  How do you use them?  Where can you get them?
  3. What kinds of data collections are built-in to Python?  What concepts do they represent?
  4. What is a "logical expression"?  What is a "state change"?
  5. What is the "for...in" statement about?  How do you use it?
  6. What is the "if" statement about?  How do you use it?
  7. Would you like a coffee break?
  8.
"""