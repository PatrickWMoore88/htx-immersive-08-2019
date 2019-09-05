#1.Madlib function
def madlib(name, subject):
    name = name_input
    subject = subject_input
    if name_input == '':
        name = 'Patrick'
    if subject_input == '':
        subject= 'Coding'
    print(f"{name}'s favorite subject is {subject}")
    print("=" * 38)
print("=" * 38)
print("[Names]'s favorite subject is [Subject]")
print("=" * 38)
name_input = input("What is the [Name]?: ")
subject_input = input("What is the [Subject]?: ")
print("=" * 38)
madlib(name_input, subject_input)
#2.Celsius to Fahrenheit conversion
def c_to_f(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return f"{temp_f}F"
temp_c_input = int(input("What is the temperature in Celsius?: "))
print(c_to_f(temp_c_input))
#3.Fahrenheit to Celsius conversion 
def f_to_c(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return f"{temp_c}C" 
temp_f_input = int(input("What is the temperature in Fahrenheit?: "))
print(f_to_c(temp_f_input))
print("=" * 38)
#4/5.is_even and is_odd functions
def is_even(num):
    return num % 2 == 0
def is_odd(num):
    return not is_even(num)
num_input = int(input("What is your number?: "))
print(is_even(num_input))
print(is_odd(num_input))
print("=" * 38)
#6/7.only_evens and only_odds functions
def only_evens(number_list):
    evens_list = []
    odds_list = []
    for nums in number_list:
        if is_even(nums):
            evens_list.append(nums)
        elif is_odd(nums):
            odds_list.append(nums)
    print(evens_list)
    print(odds_list)
number_list = [11, 20, 42, 97, 23, 10]
only_evens(number_list)
print(only_odds(number_list))
print("=" * 38)
#Medium
#1/2.Find the smallest and largest values
def smallest_and_largest(num_list):
    print(f"Given this list of numbers: {number_list}")
    print(f"The smallest value is: {min(number_list)}")
    print(f"The largest value is: {max(number_list)}")
smallest_and_largest(number_list)
print("=" * 38)
#3/4.Find the shortest and longest Strings
def shortest_and_longest(list_of_words):
    print(f"Given this list of words: {list_of_words}")
    print("The shortest word is: ", min(list_of_words, key= len))
    print("The longest word is: ", max(list_of_words, key= len))
words_list = ['Hello', 'My', 'Name', 'Is', 'Patrick']
shortest_and_longest(words_list)
print("=" * 38)

