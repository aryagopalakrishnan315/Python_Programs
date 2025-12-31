class Student:
	def __init__(self, mark1, mark2): 
		self.mark1 = mark1 
		self.mark2 = mark2

	def display_total(self):
		total = self.mark1 + self.mark2 
		print(f"Total marks: {total}")

	def __add__(self, other):
		return (self.mark1 + self.mark2) + (other.mark1 + other.mark2)


print("Enter marks for Student 1:") 
m1_1 = int(input("Subject 1: ")) 
m1_2 = int(input("Subject 2: ")) 
student1 = Student(m1_1, m1_2)
print("\nEnter marks for Student 2:") 
m2_1 = int(input("Subject 1: ")) 
m2_2 = int(input("Subject 2: ")) 
student2 = Student(m2_1, m2_2)
print("\nStudent 1:") 
student1.display_total()
print("Student 2:") 
student2.display_total()
combined_total = student1 + student2
print("\nCombined total marks of both students:", combined_total)

