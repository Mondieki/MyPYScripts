import os
import sqlite3
import time
#import admin
#if not admin.isUserAdmin():
#        admin.runAsAdmin()

os.chdir(r"/Users/MikeOndieki/Documents/Projects/MyPYScripts")              #Database's location
conn = sqlite3.connect('stations.db')
cursor=conn.execute("SELECT * FROM Stations")
os.chdir(r"/Users/MikeOndieki/Documents/Projects/MyPYScripts/audio")        #directory containing list of radio stations

"""Renames from '#LOGGER' to 'STATION NAME' """
for row in cursor:
    StationID=str(row[0])
    StationName=row[1]
    station_list=os.listdir()
    for station_name in station_list:
        if station_name.strip()[6:]==StationID:
            os.rename(station_name,StationName)                             #renames log folders to their respective Station names: i.e logger1--> RadioAsia and so on

"""Renames from '#LOG_DAY_NUMBER' to 'LOG_DATE'"""
def rename_logDays():
    log_days=os.listdir()
    for log_day in log_days:
        date_of_log=os.path.getmtime(log_day)
        log_date=time.strftime('%m-%d-%Y', time.gmtime(date_of_log))
        os.rename(log_day, log_date)

"""Renames 8 to 0900hrs"""
def rename_toHours():
    for folder in os.listdir():
        newname=str(folder + 1).zfill(2) + "00hrs"
        os.rename(folder, newname)


"""Change into Station Directory and rename the log days."""
stations=os.listdir()
for station in stations:
    if os.path.isdir(station):
        os.chdir(station)
        rename_logDays()
        os.chdir('..') 
    else:
        pass 