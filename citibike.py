#Testing out cursors

import arcpy
import datetime
from sys import exit

#Get file and create search cursor from it
InputFile = 'data/2014-07 - Citi Bike trip data.csv'
fields = ['starttime', 'start station latitude', 'start station longitude',\
 'end station latitude', 'end station longitude']
cursor = arcpy.SearchCursor(InputFile, fields)

fc = []
hr = []

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

    #Put hour in a list
    values = row.getValue('starttime'), #somehow that comma matters
    date = values[0]
    hour = date.hour
    print date, hour
    hr.append(hour)

    #End at day 2
    if date.day == 2:
        break

#Create dataset to put fc in
arcpy.CreateFileGDB_management("Data", "Output.gdb")

output = 'Data/Output.gdb/output'

#Put the fc in the dataset
arcpy.CopyFeatures_management(fc, output)

#Proejct the fc in the dataset
arcpy.DefineProjection_management(output, 32662)

arcpy.env.workspace = 'Data/Output.gdb'

#Add field to file with the hour of the day
arcpy.AddField_management('output', 'Hour', 'FLOAT')

#Run update cursor to fill it in
cursor2 = arcpy.UpdateCursor(output)
houriter = iter(hr)
count = 0

for row in cursor2:
    houriter.next()
    row.Hour = houriter
    cursor2.updateRow(row)
    count += 1
    if count % 100 == 0:
        print count

#Clean up the mess
del cursor, cursor2, row

print 'Done now'