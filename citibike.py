#Code written by vdveen
#Purpose: TBD yo

opendata = open('Citibike10.csv')
bikedata = opendata.read()
test = bikedata.split('\"\"')
for item in test:
  if item == ',':
    test.remove(',')

print type(test)

test = bikedata.split(',')
print test

newfile = open('Citibike10-2.csv', 'w')
for item in test:
  newfile.write(str(test))
newfile.close()
