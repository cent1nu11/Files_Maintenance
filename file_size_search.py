# this program will search and list files smaller than a specified byte size

import os
from datetime import datetime, timedelta
import time

dest_path = r'F:\temp'

file_size_limit = 1000

os.chdir(dest_path)

for item in os.listdir():
    if os.path.isfile(item):
        os.stat(item).st_blksize