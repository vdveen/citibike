#Testing out cursors

import arcpy
import datetime
from sys import exit

#Get file and create search cursor from it
InputFile = 'data/2014-07 - Citi Bike trip data.csv'
cursor = arcpy.SearchCursor(InputFile)

count = 0
for row in cursor:
    values = row.getValue('starttime'),
    date = values[0]
    if date.day == 2:
        exit('done')
