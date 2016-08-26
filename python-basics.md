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
some_string = "Hello!"
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

# iterate throught the list:
for item in my_list:
	print item
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
