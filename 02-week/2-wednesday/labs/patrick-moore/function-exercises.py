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
    return temp_f
temp_c_input = int(input("What is the temperature in Celsius?: "))
print(c_to_f(temp_c_input))
#3.Fahrenheit to Celsius conversion 
def f_to_c(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c 
temp_f_input = int(input("What is the temperature in Fahrenheit?: "))
print(f_to_c(temp_f_input))