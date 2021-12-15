import math
from prettytable import PrettyTable

# takes in the grades before rounding
def gradingStudents(grades):
    # loop through grades
    for i in range(len(grades)):
        # If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5
        # If the value of the grade is less than 38, no rounding occurs as the result will still be a failing grade.
        if (grades[i] % 5 == 0 or grades[i] < 38):
            continue
        else:
            next = math.ceil(grades[i] / 5) * 5
            if (next - grades[i] < 3):
                grades[i] = next

    # returns the grades after rounding as appropriate
    return grades

# Input Format
# The first line contains a single integer, n, the number of students
n = int(input('\nPlease enter number of students: '))
while (n < 1 or n > 60):
    n = int(input('Wrong input! Please enter a number between 0 and 60: '))

# Each line i of the n subsequent lines contains a single integer, grades[i].
grades = []
print('\n')
for i in range(n):
    grade = int(input('Please enter grade for student ' + str(i+1) + ': '))
    while (grade < 1 or grade > 100):
        grade = int(input('Wrong input! Please enter grade between 0 and 100 for student ' + str(i+1) + ' : '))
    grades.append(grade)

# print results
print('\n')
x = PrettyTable()
x.field_names = ["ID", "Original Grade", "Final Grade"]
original_grades = grades.copy()
final_grades = gradingStudents(grades)
for i in range(n):
    x.add_row([i+1, original_grades[i], final_grades[i]])
print(x)
print('\n')