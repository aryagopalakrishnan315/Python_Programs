class Student:
	def __init__(self, name, roll_number, marks):
		self.name = name
		self.roll_number = roll_number 
		self.marks = marks
	def display(self): 
		print(f"Name: {self.name}")
		print(f"Roll Number: {self.roll_number}") 
		print(f"Marks: {self.marks}")
	def update_marks(self, new_marks): 
		self.marks = new_marks
		print(f"Marks updated successfully to {self.marks}") 
name = input("Enter student name: ")
roll_number = input("Enter roll number: ") 
marks = float(input("Enter marks: "))
student = Student(name, roll_number, marks) 
print("\nStudent Details:")
student.display() 
new_marks = float(input("\nEnter new marks to update: ")) 
student.update_marks(new_marks)
print("\nStudent Details:") 
student.display()
