#Purpose: TBD yo

opendata = open('Citibike10.csv')
bikedata = opendata.read()
test = bikedata.split('\"\"')
for item in test:
  if item == ',':
    test.remove(',')
rawdata = opendata.read()
rawdata = rawdata.split(',')
#fuck I am missing the first and last column, gender and tripduration

print type(test)
bikedata = []

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
    else:
      bikedata.append(item)


print bikedata

test = bikedata.split(',')
print test

newfile = open('Citibike10-2.csv', 'w')
for item in test:
  newfile.write(str(test))
for item in bikedata:
  newfile.write(item)
  newfile.write(',')
  if '\r' in item:
    newfile.write('\r')
    print item
 newfile.close()
