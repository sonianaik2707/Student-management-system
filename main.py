import student
#main menu function()

student.create_csv()
def main(user = '>'):
    print('''  ====MAIN MENU====\n1. Student Record\n2. Compute Marks
    \n(Press Enter to Exit)''')

#option 1 of menu (student record)
def student_record(user = '>'):
    print('''  ====Student Record====\n1. Add student record\n2. View/search\n3. Update\n4. Delete record
    \n(Press Enter to go back)''')

#option 2 of menu(compute marks)
def compute_marks(user = '>'):
    print('''  ====Compute Marks====\n1. Enter Marks\n2. Calculate Average\n3. Calculate Grade\n4. View Result
    \n(Press Enter to go back)''')

main()
user = input('> ')

while user != '':
    #if student record is selected 
    if user == '1':
        student_record()
        detail_1 = input('> ')
        while detail_1 != '':
            if detail_1 == '>':
                student_record()
            elif detail_1 == '1':
                student.add_student()
            elif detail_1 == '2':
                pass
            elif detail_1 == '3':
                pass
            elif detail_1 == '4':
                student.delete_student()
            else:
                print('Invalid option')
            detail_1 = input("> ")

    #if compute marks is selected
    elif user == '2':
        compute_marks()
        detail_2 = input('> ')
    
        while detail_2 != '':
            if detail_2 == '>':
                compute_marks()
            elif detail_2 == '1': 
                print('Enter Marks')
            elif detail_2 == '2':
                print('Calculate Average')
            elif detail_2 == '3':
                print('Calculate Grade')
            elif detail_2 == '4':
                print('View Result')
            else:
                print('Invalid option')
            detail_2 = input('> ')
            
    main()
    user = input('> ')    

