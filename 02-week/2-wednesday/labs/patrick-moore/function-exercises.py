#1.Madlib function
def madlib(name, subject):
    name = name_input
    subject = subject_input
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
    if num % 2 == 0:
        return True
    else:
        return False
def is_odd(num):
    if is_even(num) != True:
        return True
    else:
        return False
num_input = int(input("What is your number?: "))
print(is_even(num_input))
print(is_odd(num_input))
print("=" * 38)
#6/7.only_evens and only_odds functions
def only_evens(number_list):
    evens_list = []
    for nums in number_list:
        if nums % 2 == 0:
            evens_list.append(nums)
    return evens_list
def only_odds(number_list):
    odds_list = []
    for nums in number_list:
        if nums % 2 == 1:
            odds_list.append(nums)
    return odds_list
number_list = [11, 20, 42, 97, 23, 10]
print(only_evens(number_list))
print(only_odds(number_list))
print("=" * 38)
