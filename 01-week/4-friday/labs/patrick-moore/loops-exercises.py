#1 To 10
for num in range(1, 11):
    print(num)
print("=========================================")
#N To M
starting_num = int(input("What is our starting number? "))
ending_num = int(input("What is our ending number? "))
for num in range(starting_num, ending_num + 1):
    print(num)
print("=========================================")
#Odd Numbers
for num in range(11):
    if num % 2 == 1:
        print(num)
print("=========================================")
#Print a Square
for nums in range(5):
    for nums in range(5):
        print('*', end= ' ')
    print()
print("=========================================")
#Print a Square II
rows = int(input("Enter the number of rows: "))
for nums in range(rows):
    for nums in range(rows):
        print('*', end= ' ')
    print()
print("=========================================")
#Hollow rectangle or square
rows = int(input("Height: "))
columns = int(input("Width: ")) 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if (i == 1 or i == rows or j == 1 or j == columns):
            print("*", end= "")
        else:
            print(" ", end= "")
    print()
print("=========================================")
#Triagnle
height = 4
row = 0
while row < height:
    space = height - row
    while space > 0:
        print(end= "  ")
        space= space - 1
    star= row * 2 + 1
    while star > 0:
        print("*", end= " ")
        star= star- 1
    row= row+ 1
    print()
print("=========================================")
#Triangle 2
height = int(input("Height: "))
row = 0
while row < height:
    space = height- row- 1
    while space > 0:
        print(end= " ")
        space= space- 1
    star= row+ 1
    while star > 0:
        print("*", end= " ")
        star= star- 1
    row= row+ 1
    print()
print("=========================================")
#multiplication tables
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} =", i * j)
    print("=============")
print("=========================================")
#Print A Banner
display = input("What words would you like displayed? ")
def border_msg(msg):
    row = len(msg) + 4
    h = ''.join(['*' * row])
    result = h + '\n'"* "+msg+" *"'\n' + h
    print(result)
border_msg(display)

text = input('Text? ')
text_length = len(text)
print('*' * (text_length +4)
print('*' + text+ '*')
print('*' * (text_length +4))
print("=========================================")
#Triangle Numbers
for num in range(1, 100):
    tri_num = int(num * (num + 1)/ 2)
    print(tri_num)
print("=========================================")
#Factor a Number
for i in range(1, 11):
    for j in range(1, 11):
        if i % j == 0:
            print(f"{i} / {j} =", int(i / j))
    print("=============")