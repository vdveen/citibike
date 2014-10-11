#Code written by vdveen
#Purpose: TBD yo

opendata = open('Citibike10.csv')  #Open and read file
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

print List converted

#Add neatly converted files to output file
newfile = open('Citibike10-2.csv', 'w')
for item in bikedata:
  newfile.write(item)
  newfile.write(',')
newfile.close()
