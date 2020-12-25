import csv

category = input()
sum = [0,0]
with open('ice-cream.csv', encoding='utf-8') as File:
    reader = csv.reader(File, delimiter = ",")
    for row in reader:
        print(row)
        if row[1] == category:
            sum[0] += int(row[2])
        else:
            sum[1] += int(row[2])

result = round(0.05*sum[0] + 0.01*sum[1])

print(result)
