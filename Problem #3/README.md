## CodeWars Problem #3: Century From Year

Objective: Given a year, return the century it is in.

Language: Python 3 

# Examples: 
```python
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
```

# Writeup 
So I decided to go with lists initially but I later figured out that I could use strings to do operations rather than lists. So this is my first revision of the algorithm and it works pretty well. Will try to find a cleaner solution in the future.


# Function
```python
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
```
