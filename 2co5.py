with open("text.txt", "r") as f: 
	lines = f.readlines()
lines = [line.strip() for line in lines] 
print(lines)
