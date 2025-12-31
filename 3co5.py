import csv
with open("student.csv", "r") as f: 
	csvr= csv.reader(f)
	header = next(csvr) 
	for row in csvr:
		print(row)
