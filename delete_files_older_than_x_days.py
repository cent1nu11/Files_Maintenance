import os
from datetime import datetime, timedelta
import time

dest_path = r'C:\Users\RogerWu\Downloads\Temp'
print("Today's Date: ", datetime.now())


number_of_days_old = 81
cutoff_date = datetime.now() - timedelta(number_of_days_old)

print("cutoff_date: ", cutoff_date)

time_in_secs = time.time() - (number_of_days_old * 24 * 60 * 60)

os.chdir(dest_path)
print("Current working directory : ", os.getcwd())

for item in os.listdir():
    if os.path.isfile(item):
        print("File name : ", item)
        print("os.stat : ", os.stat(item))
        print("os.stat.st_ctime : ", os.stat(item).st_ctime)
        print("st_ctime datetime : ", datetime.fromtimestamp(os.stat(item).st_ctime))
        print("")
        
 #      if datetime.fromtimestamp(os.stat(item).st_ctime) > time_in_secs:
#            os.remove(item)