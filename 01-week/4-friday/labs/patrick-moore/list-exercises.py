num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_sum = 0
for num in num_list:
    if num in num_list:
        num_sum = num_sum + int(num)
print(num_sum)
print("=========================================")
new_num_list = [10, 30, 50, 70, 90, 20, 40, 60, 80]
print(max(new_num_list))
print(min(new_num_list))
print("=========================================")
evens_list = []
for num in num_list:
    if num % 2 == 0:
        evens_list.append(num)
print(evens_list)
print("=========================================")
pos_and_neg = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
pos_list = []
neg_list = []
for num in pos_and_neg:
    if num > 0:
        pos_list.append(num)
    elif num < 0:
        neg_list.append(num)
print(pos_list)
print(neg_list)
print("=========================================")
multiply_list = [2, 4, 6, 8, 10]
new_nums = []
for num in multiply_list:
    new_nums.append(num * 3)
print(new_nums)
print("=========================================")
multiply_list_one = [2, 4, 6, 8, 10]
multiply_list_two = [1, 3, 5, 7, 9]
combo_multiply_list = [a*b for a,b in zip(multiply_list_one, multiply_list_two)]
print(combo_multiply_list)
print("=========================================")
#spot for matricies adding 


print("=========================================")
matrix_one = [[1, 2], [2, 4]]
matrix_two = [[5, 2], [1, 0]]
matrix = [[0, 0], [0, 0]]
for num_one in range(len(matrix_one)):
    for num_two in range(len(matrix_one[0])):
        matrix[num_one] [num_two] = matrix_one[num_one][num_two] + matrix_two[num_one][num_two]
print(matrix)
print("=========================================")
dup_names_list = ["Paxton", "Adia", "Alex", "Jennifer", "Patrick", "Adia", "Alex"]
new_names_list = []
for name in dup_names_list:
    if name not in new_names_list:
        new_names_list.append(name)
print(new_names_list)
print("=========================================")
#Matrix Extra Work

