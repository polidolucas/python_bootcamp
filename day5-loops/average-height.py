student_heights = input("Altura das pessoas em cm separadas por espaço: \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

n += 1
total = 0

for height in student_heights:
  total += height

average = round(total / n)

print(f"total height = {total}")
print(f"number of students = {n}")
print(f"average height = {average}")

