## CodeWars Problem #1: List Filtering 

Objective: Create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Language: Python 3

Example 

```python 
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
```
## Writeup
First problem I do on CodeWars(or one that I CAN do). This took a little bit of StackOverflow and taking a look at the docs but after realizing that the type() function can tell if a object in a list is a certain value, I took to writing a little for loop which iterates over the list and then uses the remove function after which it iterates again until all strings are removed. At this time, I wish I could find a way to keep the function going instead of having to call that function back for a second time. 

# Actual Function(Stored in main.py)
```python

l = [1,2,'a','b'] 

def filter_list(l): 
    for i in l: # Iterates over said list
        if type(i) is int: #Checks for object type.
            continue
        else:
            l.remove(i) # Remove said string.
            filter_list(l) # Repeats function again.

    return l # Returns output
```
# Current function process
```python
l = [1,2,'a','b'] #Initial output
filter_list(l) 
l = [1,2,'b'] # Removes one string but then has to callback the function again 
l = [1,2] # Final output 
```
# Desired/Optimal function process 
```python 
l = [1,2,'a','b'] #Initial output 
filter_list(l)
l = [1,2] # #Removes all strings at once without a function callback
```
## EDIT
So after conferring with [EnderBro1000](https://github.com/EnderBro1000) who is a good friend of mine, it turns out that I got pass and continue mixed up. Here is the the revisted statement that would make the function iterate without a callback.
```python
l = [1,2,'a','b']

def filter_list(l): 
    for i in l: # Iterates over said list
        if type(i) is int: #Checks for object type.
            pass
        else:
            l.remove(i) # Remove said string.

    return l # Returns output
```
So the function conundrum is solved :D 
