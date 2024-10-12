
student_names = input("Enter the list of student names separated by commas: ").split(',')


student_names = [name.strip() for name in student_names]

student_names.sort()


print("Sorted list of student names:", student_names)
