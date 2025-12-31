# Create dictionary
students = {"Anu": 85, "Ravi": 90, "Minu": 75, "Sara": 88, "Tom": 94}
print("Original Dictionary:", students)

# Access the value of Sara
print("Sara's Marks:", students["Sara"])

# Add Kiran and update Minu’s marks
students["Kiran"] = 80
students["Minu"] = 82
print("After Adding & Updating:", students)

# Delete Tom
del students["Tom"]
print("After Deleting Tom:", students)

# Display all student names
print("Student Names:", list(students.keys()))

# Print keys and values separately
print("Keys:", list(students.keys()))
print("Values:", list(students.values()))

# Sort dictionary by values (ascending)
sorted_by_values = dict(sorted(students.items()))
print("Sorted by Values:", sorted_by_values)

# Sort dictionary by keys (ascending)
sorted_by_keys = dict(sorted(students.items()))
print("Sorted by Keys:", sorted_by_keys)

# Display student with highest marks
highest = max(students, key=students.get)
print("Topper:", highest, "with", students[highest])

# Merge with another dictionary
more_students = {"Anusha": 85, "Navin": 70, "Libin": 75}
students.update(more_students)
print("After Merge:", students)