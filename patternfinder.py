#This code is a test to look for some initial patterns in the data.

opendata = open('data/Citibike-2.csv')  #Open and read file
lines = opendata.read()
line = lines.split(',')

count = 0             #Prereq definitions for the loop below
dictionary = {}
#Using dict. because value gender is after the value tripduration in the loop
#and I didn't know how to make that work with a for loop

for item in line:         #Getting the relevant columns
  count = count + 1
  if count % 9 == 1:
    trip = item.replace('\r', '')
  if count % 9 == 0:
    item = item
  if item <> '':                            #No empty values pls
    dictionary[trip] = item

#print dictionary      Look at that nice, solid dic...tionary

maletripduration = []     #Now let's put the tripduration from the dictionary in a list
femaletripduration = []   #separated by gender

for value in dictionary:
    if dictionary[value] == '1':
      maletripduration.append(int(value))

for value in dictionary:
    if dictionary[value] == '2':
      femaletripduration.append(int(value))


print 'The Average for males is:', sum(maletripduration) / len(maletripduration)
print 'The Average for females is:', sum(femaletripduration) / len(femaletripduration)
