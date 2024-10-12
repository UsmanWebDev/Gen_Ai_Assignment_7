
input_list = input("Enter a list of integers separated by commas: ").split(',')

integers = [int(num.strip()) for num in input_list]


print("First 3 elements:", integers[:3])


print("Last 2 elements:", integers[-2:])


print("List in reverse order:", integers[::-1])
