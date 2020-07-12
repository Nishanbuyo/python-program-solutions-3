import csv


class Academy:
    student_fields = ['roll', 'name', 'course', 'paid', 'remaining']

    def __init__(self,balance):
        self.balance = balance

    def display_menu(self):
        print("--------------------------------------")
        print(" Welcome to IT Academy")
        print("---------------------------------------")
        print("1. Course Inquiry")
        print("2. Register Student")
        print("3. Display All Students")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Complete Course")
        print("7. Quit")

    def __init__(self, balance):
        self.balance = balance

    def inquiry(self):
        print("........ Course List..........")
        with open("courses.csv", "r") as courses:
            reader = csv.reader(courses)
            for line in reader:
                for item in line:
                    print(item, end="\t |")
                print("\n")
        input("Press any key to continue")
        

    def registration(self):
        print("Add Student Information")
        student_data = []
        for field in self.student_fields:
            value = input("Enter " + field + ": ")
            student_data.append(value)
            if field == "paid":
                self.balance += int(value)
                student_data.append(20000-int(value))
                break

        with open("students.csv", "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([student_data])

        print("Data saved successfully")
        input("Press any key to continue")
        return

    def display_students(self):
        print("--- Student Records ---")
        with open("students.csv", "r") as f:
            reader = csv.reader(f)
            for x in self.student_fields:
                print(x, end=' \t |')
            print("\n-----------------------------------------------------------------")
            for row in reader:
                for item in row:
                    print(item, end=" \t |")
                print("\n")
        input("Press any key to continue")
        

    def update_student(self):
        print("--- Update Student ---")
        roll = input("Enter roll no. to update: ")
        index_student = None
        updated_data = []
        with open("students.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if roll == row[0]:
                        index_student = counter
                        self.balance -= int(row[3])
                        print("Student Found: at index ",index_student)
                        student_data = []
                        for field in self.student_fields:
                            value = input("Enter " + field + ": ")
                            student_data.append(value)
                            if field == "paid":
                                self.balance += int(value)
                                student_data.append(20000-int(value))
                                break
                        updated_data.append(student_data)
                    else:
                        updated_data.append(row)
                    counter += 1

        if index_student is not None:
            with open("students.csv", "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
        else:
            print("Roll No. not found in our database")

        input("Press any key to continue")

    def delete_student(self):
        print("--- Delete Student ---")
        roll = input("Enter roll no. to delete: ")
        student_found = False
        updated_data = []
        with open("students.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if roll != row[0]:
                        updated_data.append(row)
                        counter += 1
                    else:
                     student_found = True

        if student_found is True:
            with open("students.csv", "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("Roll no. ", roll, "deleted successfully")
        else:
            print("Roll No. not found in our database")

        input("Press any key to continue")

    def complete_course(self):
        print("Congratulation, you have successfully completed course")
        print("Deposit amount 20000 has been returned")
        self.balance -= 20000
        input("Press any key to continue")



academy = Academy(100000)
while True:
    academy.display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        academy.inquiry()
    elif choice == '2':
        academy.registration()
    elif choice == '3':
        academy.display_students()
    elif choice == '4':
        academy.update_student()
    elif choice == '5':
        academy.delete_student()
    elif choice == '6':
        academy.complete_course()
    else:
        break

print("Account balance at Academy = ", academy.balance)

