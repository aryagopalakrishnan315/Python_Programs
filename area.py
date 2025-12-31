import graphics.rectangle as rect
import graphics.circle as circ 
from graphics.graphics3d import cuboid, sphere 
length = float(input("Enter length of the rectangle: ")) 
breadth = float(input("Enter breadth of the rectangle: ")) 
print("Rectangle Area:", rect.area(length, breadth)) 
print("Rectangle Perimeter:", rect.perimeter(length, breadth)) 
radius = float(input("\nEnter radius of the circle: ")) 
print("Circle Area:", circ.area(radius)) 
print("Circle Perimeter:", circ.perimeter(radius)) 
l = float(input("\nEnter length of cuboid : ")) 
b = float(input("Enter breadth of cuboid : ")) 
h = float(input("Enter height of cuboid : ")) 
print("Cuboid Surface Area:", cuboid.surface_area(l, b, h)) 
print("Cuboid Volume:", cuboid.volume(l, b, h)) 
r = float(input("\nEnter radius of sphere: ")) 
print("Sphere Surface Area:", sphere.surface_area(r))  
print("Sphere Volume:", sphere.volume(r))