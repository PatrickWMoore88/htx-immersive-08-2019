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