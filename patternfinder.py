#This code is a test to look for some initial patterns in the data.

opendata = open('Citibike100-2.csv')  #Open and read file
lines = opendata.read()
line = lines.split(',')

count = 0
for item in line:
  count = count + 1
  if count % 9 == 1:
    trip = item.replace('\r', '')
    print trip
  if count % 9 == 0:
    gender = item
    print gender , 'd'