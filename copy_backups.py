# this program works for UNC and regular C:\ paths

import os
import glob
import shutil
import logging
import time
from datetime import datetime, timedelta

file_patterns_to_copy = ['M_Diff*.bak','M_Full*.bak','W_Diff*.bak','W_Full*.bak']
source_path =  r'C:\TEMP\Source'
dest_path = r'F:\TEMP\Destination'
log_path = r'F:\TEMP\Log'
number_of_days_old = 45
cutoff_date = datetime.now() - timedelta(number_of_days_old)


# create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = os.path.join(log_path, "CopyBackups_Log_from_DELLGX620.log"), level = logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()

for i in file_patterns_to_copy:
   files_path = os.path.join(source_path, i)
   files = sorted(glob.iglob(files_path), key=os.path.getmtime, reverse=True)  # for the file pattern sort  by most recent file first
   most_recent_file = os.path.basename(files[0])    #get the first indexed value from the list (which is the most recent)
   most_recent_filepath = os.path.join(dest_path, most_recent_file)

   if os.path.isfile(os.path.join(dest_path, most_recent_file)):       #check to see if the most recent file exists in the destination location
      logger.debug("The file %s is already existed at %s", most_recent_file, dest_path)
      continue

   shutil.copy2(os.path.join(source_path, most_recent_file), dest_path)
   logger.debug("%s was copied to %s", most_recent_file, dest_path)

print("Final file copy")

# delete files older than "number_of_days_old" from the destination
logger.debug(f"Deleting files older than {number_of_days_old} days old.")
print("dest_path = ", dest_path)
print("Current working directory : ", os.getcwd())
os.chdir(dest_path)                # set working directory to the destination path
print("os.chdir(dest_path) = ", os.chdir(dest_path))
print("Current working directory : ", os.getcwd())
os.chdir(dest_path)                # set working directory to the destination path


for item in os.listdir():
#    print("os.listdir()", os.listdir())
    print("datetime.fromtimestamp(os.stat(item).st_ctime) = ", datetime.fromtimestamp(os.stat(item).st_ctime))
    print("cutoff_date = ", cutoff_date)
    
    if os.path.isfile(item):
        print(item)
        if datetime.fromtimestamp(os.stat(item).st_mtime) < cutoff_date:
            print("datetime.fromtimestamp(os.stat(item).st_mtime) = ", datetime.fromtimestamp(os.stat(item).st_mtime))
            print("cutoff_date = ", cutoff_date)
            os.remove(item)
            logger.debug(f"{item} was deleted.")

# create a directory listing of the files currently in the dest_path and save as "Directory_Listing.txt"

file = open(os.path.join(log_path, 'Directory_Listing.txt'), 'w')

for root, dirname, files in os.walk(dest_path):
    for x in files:
        file.write(root + '\\' + x + '\n')
file.close()




print("Generate directory listing")

time.sleep(30)

logger.debug("System shutdown")
#os.system("shutdown /s")
print('end')