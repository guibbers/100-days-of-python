student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

heights_sum = 0
number_of_students = len(student_heights)

for height in student_heights:
    heights_sum += height

average_height = round(heights_sum / number_of_students)

print(average_height)