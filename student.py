import csv

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
        
def save_to_csv(student):
    with open("student.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            student.fname,
            student.lname,
            student.roll_no,
            student.contact,
            student.DOB,
            student.branch,
            student.semester
        ])
        
def add_student():
    fname = input('First Name: ')
    lname = input('Last Name: ')
    roll_no = input('Roll number: ')
    contact = int(input('Contact Number: '))
    DOB = input('DOB(00-00-0000): ')
    branch = input('Branch: ')
    semester = int(input('Semester: '))
    student = Student(fname,lname,roll_no,contact, DOB, branch, semester)
    save_to_csv(student)
    print('Added student record')





