class Rectangle:
	def __init__(self, length, width): 
		self.length = length
		self.width = width


	def get_area(self):
		return self.length * self.width


	def __lt__(self, other):
		print(f"Comparing areas: {self.get_area()} < {other.get_area()}") 
		return self.get_area() < other.get_area()
length1 = int(input("Enter length of Rectangle 1: ")) 
width1 = int(input("Enter width of Rectangle 1: ")) 
rect1 = Rectangle(length1, width1)

length2 = int(input("Enter length of Rectangle 2: ")) 
width2 = int(input("Enter width of Rectangle 2: ")) 
rect2 = Rectangle(length2, width2)

print("Rectangle 1 area:", rect1.get_area()) 
print("Rectangle 2 area:", rect2.get_area())
 
if rect1 < rect2:
	print("Rectangle 1 has smaller area than Rectangle 2.") 
else:
	print("Rectangle 1 does not have smaller area than Rectangle 2.")

