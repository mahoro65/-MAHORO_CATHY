#section(i)
student_marks = [78,83,90,88,75]
print(sum(student_marks))
print(f"The sum of students marks list is {sum(student_marks)}")







#section(ii)

student_marks = [78, 83, 90, 88, 75]

# Display the first mark (index 0)
first_mark = student_marks[0]
print("First mark:", first_mark)

# Display the last mark (index -1)
last_mark = student_marks[-1]
print("last mark:", last_mark)




#section(iii)
#adding 96 to the student lists
student_marks = [78,83,90,88,75]
student_marks.append(96)
print(student_marks)






#section(iv)
student_marks = [78, 83, 90, 88, 75]
index_to_update = student_marks.index(78)#indexing
student_marks[index_to_update] = 87 #updating
print(student_marks)


