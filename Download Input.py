from datetime import date
from pathlib import Path
import requests
import os
import cookiesKey

def main():

    cookies = cookiesKey.key
    print(cookies)
    baseDir = os.getcwd()

    year = os.path.basename(baseDir) # Agarra el nombre de la carpeta en la que esta este archivo, el cual es el año de la AOC

    url = "https://adventofcode.com/YEAR/day/DAY/input"
    url = url.replace("YEAR", year)
    

    today = date.today()

    maxDay = 25
    
    if today.year == int(year):
        if today.month == 12:
            if today.day < 25:
                maxDay = currentDay

    
    for day in range(1,maxDay+1):
        tempPath = Path(f"./Day {day}/")

        if tempPath.exists():
            print(f"Day {day} exists")

        else:
            print(f"Day {day} doesn't exist")


















if __name__ == "__main__":
    main()
