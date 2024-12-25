import pandas as pd
import csv
from colorama import Fore, Style

df=pd.read_csv('diamonds.csv',header=0)
ideal = []
color_types= set()

def highest_price():
    highest= df['price'].max()
    print(Fore.BLUE+f"The highest priced Diamond: {highest}$"+Style.RESET_ALL)
    
def avg_price():
    avg=df['price'].mean()
    print(Fore.RED+ f"The average price for diamond is:{avg}$"+Style.RESET_ALL)
        

def ideal_count():
    for ind, row in df.iterrows():
        cut =row['cut'] 
        if cut == 'Ideal':
            True
            ideal.append(cut)
    print(Fore.GREEN+f"There are {ideal.count('Ideal')} Diamonds with Ideal cut"+Style.RESET_ALL)
        
def count_colors():
    for ind, row in df.iterrows():
        color_types.add(row['color'])
    print(Fore.CYAN+f"There are {len(color_types)} kinds of colors,kinds:{color_types}"+Style.RESET_ALL)

def median_for_premium():
    premium_items = df[df['cut'] == 'Premium']
        
    median_carat = premium_items['carat'].median()
    print(Fore.YELLOW+f"The median carat for Premium cut is: {median_carat}"+Style.RESET_ALL)
        


def avg_carat_per_cut ():
    avg_carats = df.groupby('cut')['carat'].mean()
    for cut, avg_carat in avg_carats.items():
        print(Fore.MAGENTA+ f"The average carat for {cut} is :{avg_carat}"+ Style.RESET_ALL)
    


def avg_price_per_color ():
    avg_prices = df.groupby('color')['price'].mean()
    for color, avg_price in avg_prices.items():
        print(Fore.RED+f"The average price for {color} is :{avg_price}$"+Style.RESET_ALL)
    



    


if __name__ == "__main__":
    ideal_count()
    highest_price()
    avg_price()
    count_colors()
    avg_price_per_color()
    avg_carat_per_cut ()
    median_for_premium()
    