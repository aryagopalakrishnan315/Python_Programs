import re
word = input("Enter the word to search: ")
with open("sample.txt", "r", encoding="utf-8") as file: 
	text = file.read()
pattern = r"\b" + re.escape(word) + r"\b"
matches = re.findall(pattern, text, flags=re.IGNORECASE) 
count = len(matches)
print(f"The word '{word}' occurs {count} times in the file.")


