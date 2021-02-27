year = 1701

def century(year):
    year = str(year)
    if year.endswith("00"):
        return int(year[:2])
    elif year.endswith("00") and len(year) <= 3:
        return int(year[0])
    elif len(year) == 2:
            return 1
    elif len(year) == 3:
        return int(year[0]) + 1 
    elif len(year) == 4:
        return int(year[:2]) + 1 
    

print(century(year))