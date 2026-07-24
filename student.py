import csv
import os

#student class
class Student:
    def __init__(self, fname,lname,roll_no,contact, DOB, branch, semester):
        self.fname = fname
        self.lname = lname
        self.roll_no = roll_no
        self.contact = contact 
        self.DOB = DOB
        self.branch = branch
        self.semester = semester
        
# Write header + data
def create_csv():
    if not os.path.exists("student.csv"):
        with open("student.csv", "w", newline="") as file:
            writer = csv.writer(file)
        
            writer.writerow([
                "First Name",
                "Last Name",
                "Roll No",
                "Contact",
                "DOB",
                "Branch",
                "Semester"
            ])
        
def save_to_csv(student):
    with open("student.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            student.fname.capitalize(),
            student.lname.capitalize(),
            student.roll_no,
            student.contact,
            student.DOB,
            student.branch.upper(),
            student.semester
            ])

def read_csv():
    with open("student.csv", "r", newline="") as file:
        reader = csv.reader(file)
        return list(reader)
        
def add_student():
    fname = input('First Name: ')
    lname = input('Last Name: ')
    roll_no = input('Roll number: ')
    try:
        contact = int(input('Contact Number: '))
        if len(str(contact)) != 10:
            print('enter valid contact no.')
            return
    except ValueError:
        print('invalid')
        return  # stops function if value is invalid
    DOB = input('DOB(00-00-0000): ')
    branch = input('Branch: ')
    try:
        semester = int(input('Semester: '))
    except ValueError:
        print('Enter number only')
        return
    student = Student(fname,lname,roll_no,contact, DOB, branch, semester)
    save_to_csv(student)
    print('Added student record')


def delete_student():
    roll = input('enter the roll no.')
    rows = read_csv()
    found = False
    for row in rows:
        if row[2]== roll:
            rows.remove(row)
            found = True
            break

    if found:
        with open("student.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Student record deleted.")
    else:
        print("Roll number not found.")
