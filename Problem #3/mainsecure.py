def century(year):
   year = input("State your input: ")
    try:
      return (year + 99) // 100
    except: 
      raise Exception("Please type in valid numbers to use this program")
