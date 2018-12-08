from shutil import copyfile, copy
from datetime import date
import calendar
import os

'''
Another fine...

#############################################################################################################################################
## |||| https://mykraken.tech |||| https://mykraken.tech |||| https://mykraken.tech |||| https://mykraken.tech |||| https://mykraken.tech  ##
#############################################################################################################################################
##       /$$      /$$           /$$   /$$                    /$$                               /$$                         /$$             ##
##       | $$$    /$$$          | $$  /$$/                   | $$                              | $$                        | $$            ##
##       | $$$$  /$$$$ /$$   /$$| $$ /$$/   /$$$$$$  /$$$$$$ | $$   /$$  /$$$$$$  /$$$$$$$    /$$$$$$    /$$$$$$   /$$$$$$$| $$$$$$$       ##
##       | $$ $$/$$ $$| $$  | $$| $$$$$/   /$$__  $$|____  $$| $$  /$$/ /$$__  $$| $$__  $$  |_  $$_/   /$$__  $$ /$$_____/| $$__  $$      ##
##       | $$  $$$| $$| $$  | $$| $$  $$  | $$  \__/ /$$$$$$$| $$$$$$/ | $$$$$$$$| $$  \ $$    | $$    | $$$$$$$$| $$      | $$  \ $$      ##
##       | $$\  $ | $$| $$  | $$| $$\  $$ | $$      /$$__  $$| $$_  $$ | $$_____/| $$  | $$    | $$ /$$| $$_____/| $$      | $$  | $$      ##
##       | $$ \/  | $$|  $$$$$$$| $$ \  $$| $$     |  $$$$$$$| $$ \  $$|  $$$$$$$| $$  | $$ /$$|  $$$$/|  $$$$$$$|  $$$$$$$| $$  | $$      ##
##       |__/     |__/ \____  $$|__/  \__/|__/      \_______/|__/  \__/ \_______/|__/  |__/|__/ \___/   \_______/ \_______/|__/  |__/      ##
##                     /$$  | $$                                                                                                           ##
##                    |  $$$$$$/                                                                                                           ##
##                     \______/                                                                                                            ##
#############################################################################################################################################
## https://mykraken.tech |||| https://mykraken.tech |||| https://mykraken.tech |||| https://mykraken.tech |||| https://mykraken.tech ||||  ##
#############################################################################################################################################

...Creation.

'''

#Grab current day
myDate = date.today()

#Grab human readable day
currentDay = calendar.day_name[myDate.weekday()]

#Absolute path to source file (for backup)
sourceFile = os.path.normpath("//networkaddress/path/to/file.xlsx")

#Destination filename built with day of week appended to original name.
destinationFile = os.path.normpath("//networkaddress/path/to/backup/" + currentDay + ".xlsx")

#Copy Source to Destination (Overwrites file if it exists)
copy(sourceFile, destinationFile)
