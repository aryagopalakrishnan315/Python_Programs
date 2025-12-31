import csv
with open("book.csv", "r") as f:
    csvr = csv.reader(f)
    print("Contents of the file are:")
    for row in csvr:
        print(row)


f = open("book.csv", "r")
col = csv.reader(f)
print("The specific columns are:")
for i in col:
    print(i[0], i[1], i[3])
