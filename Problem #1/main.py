# Main List to input 
l = [1,2,'a','b'] #Sample list

def filter_list(l): # Main function
    for i in l: # Iterates over said list
        if type(i) is int: #Checks for object type.
            pass # Uses pass rater than continue.
        else:
            l.remove(i) # Remove said string.

    return l # Returns output
            

filter_list(l) # Executes function


