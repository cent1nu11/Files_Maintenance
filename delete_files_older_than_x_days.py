# this program will take delete any files in a directory (dest_path) that are older than
# a certain number of days specified (number_of_days_old)
# it does not delete any subdirectories within the main directory

import os
from datetime import datetime, timedelta
import time

dest_path = r'F:\temp'
print("Today's Date: ", datetime.now())

number_of_days_old = 45
cutoff_date = datetime.now() - timedelta(number_of_days_old)

print("Cutoff_date: ", cutoff_date)

time_in_secs = time.time() - (number_of_days_old * 24 * 60 * 60)

os.chdir(dest_path)
print("Current working directory : ", os.getcwd())
print("")

for item in os.listdir():
    if os.path.isfile(item):
        print("File name : ", item)
        print("os.stat : ", os.stat(item))                                                  # stats information about the file
        print("os.stat.st_ctime : ", os.stat(item).st_ctime)                                # create date of the file (in seconds)
        print("st_ctime datetime : ", datetime.fromtimestamp(os.stat(item).st_ctime))       # create date of the file (in datetime format)
        print("")
        
        if datetime.fromtimestamp(os.stat(item).st_ctime) > cutoff_date:
            os.remove(item)