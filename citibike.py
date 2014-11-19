#Testing out cursors

import arcpy
import datetime
from sys import exit

#Retrieve file and create update cursor from it
InputFile = 'data/2014-07 - Citi Bike trip data.csv'
fields = ['starttime', 'start station latitude', 'start station longitude',\
 'end station latitude', 'end station longitude']
cursor = arcpy.da.SearchCursor(InputFile, fields)

#Create dataset to put fc in
try:
    arcpy.CreateFileGDB_management("Data", "Output.gdb")
except:
    print 'GDB already in place'

#Set the dataset as workspace
arcpy.env.workspace = 'Data/Output.gdb'

#Define unique path name for the line map
linemap = arcpy.CreateUniqueName('linemap')
linemap = linemap[16:]
output = 'Data/Output.gdb/' + linemap

print linemap, type(linemap)

#Create Feature Class to populate
arcpy.CreateFeatureclass_management('Data/Output.gdb', linemap, \
'POLYLINE', None, 'DISABLED', 'DISABLED', 32662)

#Add field to FC with the hour of the day
arcpy.AddField_management(output, 'Hour', 'FLOAT')

#Create empty lists to append to
#fc = []
#hr = []

#Create insertcursor for populating the FC
fields2 = ['SHAPE@', 'Hour']
inscursor = arcpy.da.InsertCursor(output, fields2)

for row in cursor:
    #Get the coordinates of the start and end
    startLat = row[1]
    startLon = row[2]
    endLat = row[3]
    endLon = row[4]

    #Make two points in Arcpy
    start = arcpy.Point(startLon,startLat,None,None,0)
    end = arcpy.Point(endLon,endLat,None,None,1)

    #Put them in an array
    triplineArray = arcpy.Array([start,end])

    #Create line between the two
    tripline = arcpy.Polyline(triplineArray)

    #Put hour in a list
    values = row[0], #somehow it crashes without this comma
    date = values[0]
    hour = date.hour
    print date, hour

    #Put point and hour in the FC with the InsertCursor
    newRow = [tripline,hour]
    inscursor.insertRow(newRow)

    #End at day 2
    if date.day == 2:
        break

exit("NO PASS")

#Put the fc in the dataset
arcpy.CopyFeatures_management(point, output)

#Project the fc in the dataset
arcpy.DefineProjection_management(output, 32662)

#Clean up the mess
del cursor, inscursor, row

print 'Done now'