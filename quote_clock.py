import json
import os
import schedule
import time
from datetime import datetime as dt
from rich import print as rprint



def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


with open("formatted_quotes.json", "r") as file:
    formatted_data = json.load(file)



def extract_time():
    """Takes time object as argument, e.g. time.localtime()"""
    current_time = dt.now()
    hour = current_time.hour
    minute = current_time.minute
    key_ = f"{hour:02}:{minute:02}" # Left pad 1 digit numbers with 0
    quote = formatted_data.get(key_)
    clear()
    rprint(f"{quote["Quote"]}")
    rprint(f"\t-From [italic]{quote["Title of book"]}[/italic] by"
           f" {quote['Author']}")


if __name__ == "__main__":
    extract_time()
    schedule.every().minute.at(':00').do(extract_time)
    while True:
        while True:
            schedule.run_pending()
            time.sleep(.1)
