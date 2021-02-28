year = input("Enter your input: ")

def century(year):
    year = str(year)
    if year.endswith("00") and len(year) > 5:
        return int(year[0])
    elif year.endswith("00") and len(year) <= 3:
        return int(year[0])
    elif len(year) == 1 or len(year) == 2 and int(year) >= 1:
            return 1
    elif len(year) == 3:
        return int(year[0]) + 1 
    elif len(year) == 4:
        return int(year[:2]) + 1 
    elif len(year) < 5: 
        return 'Please input a integer with 4 digits or less.' 
    elif int(year) <= -1:
        return 'Please input a integer with positive values.'
    else: 
        return 'Please input a valid value to use this program correctly'
    

print(century(year))