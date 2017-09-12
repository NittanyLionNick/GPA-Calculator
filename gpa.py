pts = -1234567890
cred = int(input("Please enter the number of credits for the course: "))
print(cred)
grade = input("Please enter your letter grade: ")
print(grade)
if grade == "A":
   pts = 4.0
elif grade == "A-":
   pts = 3.67
elif grade == "B+":
   pts = 3.33
elif grade == "B":
   pts = 3.00
elif grade == "B-":
   pts = 2.67
elif grade == "C+":
   pts = 2.33
elif grade == "C":
   pts = 2.00
elif grade == "D":
   pts = 1.00
elif grade == "F":
   pts = 0.0
else:
   print("Invalid grade!")
if pts >= 0.0:   
	points = cred * pts
	print("You get", points, "GPA points for that course.")
