def main_menu():
    students = []
    while True:
        print("""ENROLLMENT SYSTEM
        1. ENROLL NEW STUDENT
        2. VIEW ALL STUDENTS
        3. SEARCH STUDENT
        4. EXIT
        """)
        choice = input("Choose (1-4): ")
        if choice == '1':
            new_entry = enroll_student()
            students.append(new_entry)
            print(f"Congrats! Student {new_entry['Name']} has been enrolled!")
        elif choice == '2':
            if not students:
                print("No students were enrolled!")
            else:
                for student in students:
                    print(student)
        elif choice == '3':
            pass
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid Choice!")


def enroll_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    tuition = 0

    majors = ('Computer Science', 'Art', 'Business', 'General Education')
    major = input("""Choose a Major:
    Computer Science
    Art
    Business
    Otherwise, General Education
     """).title()

    if major == 'Computer Science':
        tuition = 5000
    elif major == 'Art':
        tuition = 3000
    elif major == 'Business':
        tuition = 4000
    elif major not in majors or major == 'General Education':
        if major != 'General Education':
            major = 'General Education'
            tuition = 2000
        else:
            tuition = 2000

    new_student = {
        "Name": name,
        "Age": age,
        "Major": major,
        "Tuition": tuition,
    }
    return new_student



main_menu()
