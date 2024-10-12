
marks_dict = {
    'Math': [85, 90, 78],
    'Science': [92, 88, 84],
    'English': [79, 83, 91]
}


for subject, marks in marks_dict.items():
    average = sum(marks) / len(marks)
    print(f"Average marks in {subject}: {average:.2f}")
