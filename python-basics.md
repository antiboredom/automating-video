# Python Basics

Here's a very quick intro to Python. If you're interested in learning more, I recommend Zed Shaw's [Learn Python the Hard Way](https://learnpythonthehardway.org/book/).

## Hello World

To run a python script, just type ```python scriptname.py``` from the command line.

Here's a basic example.

Make a new file called ```hello.py``` and stick this in there:

```python
print "hello"
```

From the terminal, run:

```
python hello.py
```

You should see "Hello" on the screen.

## Variables

You don't need to declare variable types in python, or even that something is a variable.

```python
a_number = 1 # an integer
another_number = 5.1 # a float
some_string = "Hello!" # a string
some_boolean = True #notice the capitalization on booleans
a_list = ["a bunch", "of", "stuff", a_number, some_string]
```


## Lists

A list is an ordered collection of things.

```python

# make an empty list
my_list = []

# add something to our list with the "append" method
my_list.append("hi") # the list will now look like this: ["hi"]

# add some more stuff
my_list.append(45)
my_list.append(100.2)
my_list.append("whatever")

# now our list will look like this:
# ["hi", 45, 100.2, "whatever"]

# add one list to another
my_list = my_list + [4, 5, 6]

# now, like this: ["hi", 45, 100.2, "whatever", 4, 5, 6]

# you can access individual items in the list by referrring to their index value
print my_list[0] # prints "hi"
print my_list[2] # prints 100.2

# use negative numbers to start at the back
print my_list[-1] # prints "6" - the last item

# you can access part of a list with a ":"
my_list[1:3] # will be [45, 100.2, "whatever"]

# iterate throught the list:
for item in my_list:
	print item
	
	
# you can also have a list of lists, like so
cool_list = [[1,2,3], ["hello", "friend"]]

print cool_list[0][2] # prints 2
print cool_list[1][0] # prints "hello"
```

## Dictionaries

Dictionaries are key-value pairs. They are like lists, but they are not ordered, and instead of accessing items with a number, you use a key, which could be a string, number or other python object.

```python

# create an empty dictionary
my_dict = {}

# create a dictionary with values
my_dict = {"name": "Sam", "height": "short"}

# pull values out of a dictionary
print my_dict["name"] # prints "Sam"

# override or insert new items
my_dict["name"] = "Todd" # changes "name" to "Todd"
my_dict["last_name"] = "Anderson" # adds a new key "last_name" with the value "Anderson"
```

## Flow control

```python

name = "Sam"

if name == "Sam":
	print "Hi Sam!!!!!"
else:
	print "Hi " + name
```

## Command Line Arguments
```python
import sys

name = sys.argv[1]
print "Hi " + name
```
