#Code written by vdveen
#Purpose: TBD yo

opendata = open('Citibike10.csv')
rawdata = opendata.read()
rawdata = rawdata.split('\r')
print len(rawdata)
print rawdata
bikedata = rawdata

for item in rawdata:
  if item == '""tripduration':
    item = 'tripduration'
    bikedata.append(item)

  elif item == '""""starttime""':
    item = 'starttime'
    bikedata.append(item)

  elif item.startswith('""') and item.endswith('""'):
    item = item[2:-2]
    if item.endswith('year') or len(item) == 1:
      item = item + '\r'
    bikedata.append(item)


print bikedata


newfile = open('Citibike10-2.csv', 'w')
for item in bikedata:
  newfile.write(item)
  newfile.write(',')

newfile.close()
