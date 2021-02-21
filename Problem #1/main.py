# Main List to input 
l = [1,2,'a','b'] #Sample list

def filter_list(l): 
    for i in l: # Iterates over said list
        if type(i) is int: #Checks for object type.
            continue
        else:
            l.remove(i) # Remove said string.
            filter_list(l) # Repeats function again.

    return l # Returns output
            

filter_list(l) # Executes function


