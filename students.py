students = {}

def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks out of 100: "))
    students[name] = marks
    print(f"{name} added with {marks} marks.\n")

def display_all():
    print("\nAll Students:")
    for name, marks in students.items():
        print(f"{name}: {marks}")

def display_topper():
    topper = max(students, key=students.get)
    print(f"\nTopper: {topper} with {students[topper]} marks")

def run():
    while True:
        print("\n1. Add Student\n2. Display All\n3. Show Topper\n4. Exit")
        ch = input("Choose: ")
        if ch == '1': add_student()
        elif ch == '2': display_all()
        elif ch == '3': display_topper()
        elif ch == '4': break
        else: print("Invalid choice")

run()
