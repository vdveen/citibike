#Testing out cursors

import arcpy
import os
import datetime
from sys import exit

#Retrieve file and create update cursor from it
InputFile = 'data/2014-07 - Citi Bike trip data.csv'
fields = ['starttime', 'start station latitude', 'start station longitude',\
 'end station latitude', 'end station longitude', 'stoptime']
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
print output

#Create Feature Class to populate
arcpy.CreateFeatureclass_management('Data/Output.gdb', linemap, \
'POLYLINE', None, 'DISABLED', 'DISABLED', 4326)

#Add fields to FC with the start and endtime and the date
arcpy.AddField_management(output, 'StartTime', 'DATE')

arcpy.AddField_management(output, 'EndTime', 'DATE')

#Create insertcursor for populating the FC
fields2 = ['SHAPE@', 'StartTime', 'EndTime']
inscursor = arcpy.da.InsertCursor(output, fields2)

count = 0
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
    sr = arcpy.SpatialReference(4326)

    #Create line between the two
    tripline = arcpy.Polyline(triplineArray, sr)

    #Get the start time from the source data
    values = row[0], #somehow it crashes without this comma
    starttime = values[0]

    #Get the end time from the source data
    values = row[5],
    endtime = values[0]

    #Put point and hour in the FC with the InsertCursor
    newRow = [tripline, starttime, endtime]
    inscursor.insertRow(newRow)

    #Keep track of amount of features done
    count += 1
    if count % 1000 == 0:
        print count

    #End at day 2
    if starttime.day == 2:
        break

#Put the results of the insert cursor in a layer file
arcpy.MakeFeatureLayer_management(output,'temp')
outputname = 'Data/' + linemap + '.lyr'
print outputname
arcpy.SaveToLayerFile_management('temp', outputname)

#Get the layer file so it can be edited
layer = arcpy.mapping.Layer(outputname)
timelayer = arcpy.mapping.Layer('assets/Time.lyr')

#Open empty map document
mxd = arcpy.mapping.MapDocument('assets/Empty.mxd')
df = arcpy.mapping.ListDataFrames(mxd)[0]
print df
#Copy time settings from time layer:
arcpy.mapping.UpdateLayerTime(df, layer, timelayer)

#Add layer to map document
arcpy.mapping.AddLayer(df, layer)
arcpy.RefreshActiveView

lyrtime = layer.time
print lyrtime.startTime, lyrtime.endTime
print lyrtime.isTimeEnabled

#Save to copy
arcpy.env.overwriteOutput = True
layer.saveACopy('Full.mxd')
print arcpy.GetMessages()

arcpy.env.workspace = 'C:/Users/anne.vanderveen/Desktop/citibike/assets'
#Attempt to crunch out images
df.time.currentTime = df.time.startTime
while df.time.currentTime <= df.time.endTime:
    # An example str(newTime) would be: "2008-12-29 02:19:59"
    # The following line splits the string at the space and takes the first
    # item in the resulting string.
    fileName = arcpy.CreateUniqueName('linemap') + ".png"
    arcpy.mapping.ExportToPNG(mxd, fileName, df, 1080, 720)
    df.time.currentTime = df.time.currentTime + df.time.timeStepInterval

#Clean up the mess
del cursor, inscursor, row, mxd, df, layer, outputname

print 'Done now'