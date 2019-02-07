# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

#Benjamin Page
#2/7/2019
#Input type for each exam was different. Misnamed variable for exam_three. Variable 'grades' was not represented as a set. 'grades' was misspelled in 'avg=sum/len(grades)'.
#Elif statement on letter_grade = "F" should be else statement.
#"For grade in grade" statement had no defined variables tied to it.
#Final two print statements were not in closed parentheses.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = {exam_one,exam_two,exam_three}
sum = 0
for el in grades:
  sum = sum + el

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

print("Exam: " + str(grades))

print("Average: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade is "F":
    print("Student is failing.")
else:
    print("Student is passing.")
