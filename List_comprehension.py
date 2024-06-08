#list comprehension = a way of creating a new list with less syntax
#                     can mimic certain lambda functions, easier to read
#                     list = [expression (if/else)for item in iterable, if conditional]

squares = []                    #create an empty list
for i in range(1,11):           #create a for loop
    squares.append(i * i)       #define what each loop iteration should do
print(squares)

squares = [i*i for i in range (1,11)]
print(squares)

students = [10,25,35,45,41,65,78,85,99,14]
#passed_student = list(filter(lambda a: a >=60, student))
#print(passed_student)

#passed_student = [i for i in student if i>= 60]
passed_student = [i if i >=60 else "failed" for i in students]
print(passed_student)

