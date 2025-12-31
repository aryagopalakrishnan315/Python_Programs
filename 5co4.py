class Student:
	def __init__(self, name): 
		self.name = name

	def display_name(self): 
		print("Student Name:", self.name)
class MCAStudent(Student):
	def __init__(self, name, semester): 
		super().__init__(name) 
		self.semester = semester

	def display_semester(self): 
		print("Semester:", self.semester)

name = input("Enter the student's name: ") 
semester = input("Enter the semester: ")
mca_student = MCAStudent(name, semester)
mca_student.display_name() 
mca_student.display_semester()

