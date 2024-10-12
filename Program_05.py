
input_list = input("Enter a list of elements separated by commas: ").split(',')


unique_list = list(set([item.strip() for item in input_list]))


print("List without duplicates:", unique_list)
