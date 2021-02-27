## CodeWars Problem #2: Square Every Digit

Objective: Square every digit of a number and concatenate them.

Language: Python 3 

# Examples: 
Run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.

Note: The function accepts an integer and returns an integer.

# Writeup 
This one was harder than expected. While I wanted to put them into a for loop, I had problems with putting it all into a for loop so I did a list for each operation it had to do. Very inefficent but it works. Probably going to talk to more friends and try to find a better revision. It works for now and I'm proud of it!
# Function(First Revision)
```python
def square_digits(num): 
    num = str(num)
    list = [digit for digit in num]
    list2 = [ int(i) for i in list ]
    list3 = [ i **2 for i in list2 ]
    list4 = [ str(i) for i in list3 ]
    output = ""
    for i in list4:
       output += i 
    output = int(output)
    return output
```


