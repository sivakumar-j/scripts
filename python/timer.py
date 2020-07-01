#!/usr/bin/env python3.6

#Local time output will be in below format
#%X hh:mm:ss of it
#time.struct_time(tm_year=2020, tm_mon=7, tm_mday=1, tm_hour=7, tm_min=59, tm_sec=39, tm_wday=2, tm_yday=183, tm_isdst=0)

#Mktime format will be in below format
#1593590379.0 which is seconds. Subtracted from 1970 Jan 1st Midnight. Need to check the fact

#import time -- this import all modules of time. To avoid this we use below syntax
from time import localtime, mktime, strftime


start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")


#Wait for user to stop timer
input("Press 'Enter' key to stop timer ")


stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)


print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")
print(f"\n")
print(f"Local time in its original format         :  \n{start_time} \n")
print(f"Mktime of startime in its original format : {mktime(start_time)}" )

