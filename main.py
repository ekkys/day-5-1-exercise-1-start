# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

print(student_heights)

sum_height = 0
count_student = 0
for height in student_heights:
  # print(height)
  sum_height += height
  count_student += 1
height_average = round(sum_height / count_student)
print(f"Total Height : {sum_height}")
print(f"Total student:{count_student}")
print(f"Height Average : {height_average}")



