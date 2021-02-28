from word2number import w2n

print("Welcome to Ty's Medieval Century Calculator! Please input a number and find out what century your year belongs to!")
def centuryInit(): 
    init = input("Would you like to use numbers or words to calculate your century? Please type n for Numbers and w for words or q if you just want to quit: ")
    if init == "n":
        centuryActualNumbers()
    elif init == "w":
        centuryActualWords()
    elif init == "q": 
        print("Thank you for using Ty's Medieval Century Calculator!")
    else: 
        print("Please either input n for Numbers and w for words or q if you just want to quit")
        centuryInit()
        

def centuryAgain():
    input = input("Would you like to try to calculate more numbers? Please put y for yes or n for no: ")
    if input == "y":
        centuryInit()
    else: 
        print("Thank you for using Ty's Medieval Century Calculator!")

    
def centuryActualNumbers():
    year = input("State your numbers fellow knight: ") 
    try:
        year = int(year)
        x = (year + 99) // 100
        print(f"The year {year} belongs to the Century of {x}! Huzzah!")
        centuryAgain()
    except:
         print("I'm sorry fellow knight but the program insists on receiving numbers!")
         print("Please try again fellow knight!")
         centuryAgain()

def centuryActualWords():
    print("A good example of using words are two thousand and two")
    year = input("State your words fellow knight: ") 
    try: 
        x = w2n.word_to_num(year)
        year = int(x)
        x = (year + 99) // 100
        print(f"The year {year} belongs to the Century of {x}! Huzzah!")
        centuryAgain()
    except:
         print("I'm sorry fellow knight but the program insists on words with spaces!")
         
         centuryAgain()

         


centuryInit()
        
    
