colour1=input("Enter colours separated by comma:").split(",") 
print("first colour",colour1[0]) 
print("last colour",colour1[-1]) 
colour2=input("Enter colours separated by comma:").split(",") 
difference =[] 
for a in colour1: 
 if a not in colour2: 
  difference.append(a) 
print(difference) 
