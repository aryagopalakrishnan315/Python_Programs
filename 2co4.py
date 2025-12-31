class Student:
	def __init__(self, name, mark1, mark2): 
		self.name = name
		self.mark1 = mark1 
		self.mark2 = mark2
	def total(self):
		return self.mark1 + self.mark2 
	def display(self):
		print(f"Student Name: {self.name}") 
		print(f"Marks in Subject 1: {self.mark1}") 
		print(f"Marks in Subject 2: {self.mark2}") 
		print(f"Total Marks: {self.total()}")
name = input("Enter student name: ")
mark1 = float(input("Enter marks in Subject 1 (out of 100): ")) 
mark2 = float(input("Enter marks in Subject 2 (out of 100): ")) 
student = Student(name, mark1, mark2) 
print("\nStudent Details:") 
student.display()
