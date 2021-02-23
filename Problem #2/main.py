num = 9119

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

print(square_digits(num))


