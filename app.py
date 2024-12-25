import pandas as pd
from enum import Enum
if __name__ == "__main__":
    
    df = pd.read_csv('diamond.csv')

    user_result = ""
    class enum(Enum):
        Exit = 0
        MOST_EXPENSIVE=1
        AVERAGE_PRICE = 2
        COUNT_IDEAL=3
        COUNT_BY_COLOR = 4
        MEDIAN = 5
        AVERAGE_CARAT_PER_CUT = 6
        AVERAGE_PRICE_PER_COLOR = 7
        #1 most expensive diamond
def most_expensive():
        priced = list(df['price'])
        print(f"the highest price is - {max(priced)}")
    #2averaged of diamond
def avaraged():
        priced = list(df['price'])
        print(f"the avarage is {(priced)}")
     #menu
def menu():
        for act in enumerate: print(f"{act.value} - {act.name}")
        return input("what is your selection?")
    #3 ideal cut
def ideal_cut():
        ideal = list(df['cut']) 
        count = 0
        for x in ideal:
            if x == 'Ideal':
                count +=1
        print(count)
    #4color diamond
def colored():
        colors= list(df['color'])
        userchoice = input("choose a color? ")
        countC=0
        for x in colors:
            if x == userchoice:
                countC +=1
        print(f"there are {countC}")
    #5 median diamond
def median():
        collums,rows =df.shape
        print(collums)
    #6 average_carat_per_cut
def average_carat_per_cut():
        average_carat = df.groupby('cut')['carat'].mean()
        print("Average carat per cut:")
        print(average_carat)
    #7
def average_price_per_color():
        average_price = df.groupby('color')['price'].mean()
        print("Average price per color:")
        print(average_price)
        
      
while True:
        user_result = enum(int(menu()))
        if user_result == enum.Exit : exit()
        elif user_result == enum.MOST_EXPENSIVE: most_expensive()
        elif user_result == enum.AVERAGE_PRICE: avaraged()
        elif user_result == enum.COUNT_IDEAL: ideal_cut()
        elif user_result == enum.COUNT_BY_COLOR: colored()
        elif user_result == enum.MEDIAN: median()
        elif user_result == enum.AVERAGE_CARAT_PER_CUT: average_carat_per_cut()
        elif user_result == enum.AVERAGE_PRICE_PER_COLOR:average_price_per_color()

        
        