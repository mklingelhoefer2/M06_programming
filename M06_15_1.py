# Mark Klingelhoefer
# Module 6
# Program runs through a loop 3 different times that waits
# a random number of seconds then prints the date and time

import multiprocessing
from datetime import date
from datetime import datetime
from time import sleep
import random

# Sleep for a number of seconds and print current date and time
def current_time(seconds):
    sleep(seconds)
    today = datetime.now()
    print(today)

# Create a random number between 0 and 1, loop 3 times
if __name__ == '__main__':
    for i in range(3):
        seconds = random.random()
        process = multiprocessing.Process(target=current_time, args=(seconds,))
        process.start()