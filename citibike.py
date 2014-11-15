#Testing out cursors

import arcpy
import datetime
from sys import exit

#Get file and create search cursor from it
InputFile = 'data/2014-07 - Citi Bike trip data.csv'
cursor = arcpy.SearchCursor(InputFile)

fc = []

for row in cursor:
    #get the coordinates of the start and end
    startLat = row.getValue('start station latitude')
    startLon = row.getValue('start station longitude')
    endLat = row.getValue('end station latitude')
    endLon = row.getValue('end station longitude')

    #make two points in Arcpy
    start = arcpy.Point(startLon,startLat,None,None,0)
    end = arcpy.Point(endLon,endLat,None,None,1)

    #Put them in an array
    triplineArray = arcpy.Array([start,end])

    #Create line between the two
    tripline = arcpy.Polyline(triplineArray)

    #Put them in a fc
    fc.append(tripline)

    values = row.getValue('starttime'),
    date = values[0]
    if date.day == 2:
        break

arcpy.CopyFeatures_management(fc, r"E:\UGIS\G567\GitHub\citibike\best.shp")
print 'Copied'


