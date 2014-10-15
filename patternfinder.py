#This code is a test to look for some initial patterns in the data.

opendata = open('Citibike100-2.csv')  #Open and read file
lines = opendata.read()
line = lines.split(',')

count = 0
dictionary = {}

for item in line:         #Getting the relevant columns
  count = count + 1
  if count % 9 == 1:
    trip = item.replace('\r', '')
    print trip
  if count % 9 == 0:
    gender = item
    print gender , 'd'
  dictionary[trip] = item

print dictionary
