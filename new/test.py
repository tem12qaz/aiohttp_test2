import csv

myData = [['1;2;3;456;7'],
          ['1;2;2;4dsc6;7'],
          ['dscsd1;fref;3;456;7'],
          ['ssdc;234r34;3;456;7']]

myFile = open('ice-cream.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

print("Writing complete")
# 
# a= {'c':5,'f':8,'g':3}
#
# mydict = {'george': 16, 'amber': 19}
# print(list(mydict.keys())[list(mydict.values()).index(16)])
