#Code written by vdveen
#Purpose: cleaning up the original data.
#So the original csv file has a million apostrophes, which I
#first need to get rid of.

opendata = open('Citibike100.csv')  #Open and read file
rawdata = opendata.read()
rawdata = rawdata.replace('\r', ',')  #Replace newlines with commas
rawdata = rawdata.split(',')       #Then split on commas

#New list to add to
bikedata = []

#Check all items in data, remove brackets, convert it into a flawless file.
for item in rawdata:
  if item == '""tripduration':
    item = 'tripduration'
    bikedata.append(item)

  elif item == '""""starttime""':
    item = 'starttime'
    bikedata.append(item)

  elif item.startswith('""') and item.endswith('"""'):
      item = item[2:-3]
      bikedata.append(item)

  elif item.startswith('""') and item.endswith('""'):
    item = item[2:-2]
    bikedata.append(item)


  elif item.startswith('"'):
    item = item[1:]
    item = '\r' + item
    bikedata.append(item)

  elif item == '\N':
    item = 'null'
    bikedata.append(item)

print 'Cleaned up data'
#Here, the original data is fully cleaned up.
#This part of the script creates a file for the cleand up data.
bikefile = open('Citibike100clean.csv', 'w')
for item in bikedata:
  bikefile.write(item)
  bikefile.write(',')

#So, done cleaning, now we create a new file to put the
#relevant data in, stripping out all unnecessary stuff.
newfile = open('Citibike100-2.csv', 'w')
count = 0

#Now, lets remove the unneeded columns, shall we?
for item in bikedata:
  count = count + 1           #Counts what number the item is
  if count % 15 == 4:           #Don't write start station ID
    newfile.write('')
  elif count % 15 == 5:         #Don't write start station name
    newfile.write('')
  elif count % 15 == 8:         #Don't write end station ID
    newfile.write('')
  elif count % 15 == 9:         #Don't write end station name
    newfile.write('')
  elif count % 15 == 9:         #Don't write end station name
      newfile.write('')
  elif count % 15 == 12:        #Don't write bike ID
      newfile.write('')
  elif count % 15 == 13:        #Don't write subscriber type
    newfile.write('')
  else:                         #Write everything else
    newfile.write(item)
    newfile.write(',')

#Finally, the file is how we want it. Let's save it to the file!
newfile.close()
