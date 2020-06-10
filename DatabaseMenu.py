import shelve
import os

def clearscreen():
    os.system('cls')
    
def addrecord():
# Key is the student number
    number = input('Please input student number: ')
    title = input('Student title: ')
    forename = input('Student forename: ')
    surname = input('Student surname: ')
    module = input('Course module: ')
    coursemark = input('Student coursemark: ')
    exammark = input('Student exammark: ')
# Checks if number, coursemark and exammark only contain decimal digits
    if number.isdigit() == False:
        number = input('Student number entered contains a letter, please input again: ')
    if coursemark.isdigit() == False:
        coursemark = input('Coursemark entered contains a letter, please input again: ')
    if exammark.isdigit() == False:
        exammark = input('Exammark entered contains a letter, please input again: ')
# Checks if title, forename and surname only contain alphabetic characters
    if title.isdigit() == True:
        title = input('Title entered contains a number, please input again: ')
    if forename.isdigit() == True:
        forename = input('Forename entered contains a number, please input again: ')
    if surname.isdigit() == True:
        surname = input('Surname entered contains a number, please input again: ')
# Checks if module contains two upper case characters followed by four decimal digits
    if module[0:1].islower() == True or module[2:5].isalpha() == True:
        module = input('Module must be inputted in the format of two uppercase letters followed by four decimal digits, please input again: ')
# Creates list to store the student info    
    student_info = []
    student_info.append(number)
    student_info.append(title)
    student_info.append(forename)
    student_info.append(surname)
    student_info.append(module)
    student_info.append(coursemark)
    student_info.append(exammark)
# Joins the list into a string
    student = ' '.join(student_info)
# Adds a new record to the database
    db = shelve.open(module)
# Check the key(student number) isn't taken
    if number in db:
        print("Student %s already exists." % number)
    else:
        db[number] = student
        print("Student %s added to database." % number)
    db.close()

def displayrecord():
# Extracts and displays record from the database
# Prompts user for the student number and module
    number = input('Please select student number: ')
    module = input('Please select student module: ')
# Checks if number only contains decimal digits
    if number.isdigit() == False:
        number = input('Student number entered contains a letter, please input again: ')    
# Checks if module contains two upper case characters followed by four decimal digits
    if module[0:1].islower() == True or module[2:5].isalpha() == True:
        module = input('Module must be inputted in the format of two uppercase letters followed by four decimal digits, please input again: ')    
    db = shelve.open(module)
    if number in db:
        value = db[number]
        print(value)
    else:
        print("Student number %s does not exist." % number)
    db.close()

def updaterecord():
# Updates a record in the database
# Prompts user for the student number and module
    number = input('Please select student number: ')
    module = input('Please select student module: ')
# Checks if number only contains decimal digits
    if number.isdigit() == False:
        number = input('Student number entered contains a letter, please input again: ')    
# Checks if module contains two upper case characters followed by four decimal digits
    if module[0:1].islower() == True or module[2:5].isalpha() == True:
        module = input('Module must be inputted in the format of two uppercase letters followed by four decimal digits, please input again: ')
    db = shelve.open(module)
    if number in db:
        while True:
            updateoption = input("""
                    Student Number: %s  Module: %s
                    Update Record

                    (1) Title
                    (2) Forename
                    (3) Surname
                    (4) Coursemark
                    (5) Exammark
                    (6) Cancel update

                    Please select the record to be updated:- """ % (number, module))
            if updateoption == '1':
                student = db[number]
                student_info = student.split(' ')
                student_info[1] = input("""
                    Old title was '%s'.
                    New title: """ % student_info[1])
                student = ' '.join(student_info)
                db = shelve.open(module)
                db[number] = student
                db.close()
                print("Record updated.")
            elif updateoption == '2':
                student = db[number]
                student_info = student.split(' ')
                student_info[2] = input("""
                    Old Forename was '%s'.
                    New Forename: """ % student_info[2])
                student = ' '.join(student_info)
                db = shelve.open(module)
                db[number] = student
                db.close()
                print("Record updated.")
            elif updateoption == '3':
                student = db[number]
                student_info = student.split(' ')
                student_info[3] = input("""
                    Old surname was '%s'.
                    New surname: """ % student_info[3])
                student = ' '.join(student_info)
                db = shelve.open(module)
                db[number] = student
                db.close()
                print("Record updated.")
            elif updateoption == '4':
                student = db[number]
                student_info = student.split(' ')
                student_info[5] = input("""
                    Old coursemark was '%s'.
                    New coursemark: """ % student_info[5])
                student = ' '.join(student_info)
                db = shelve.open(module)
                db[number] = student
                db.close()
                print("Record updated.")
            elif updateoption == '5':
                student = db[number]
                student_info = student.split(' ')
                student_info[6] = input("""
                    Old exammark was '%s'.
                    New exammark: """ % student_info[6])
                student = ' '.join(student_info)
                db = shelve.open(module)
                db[number] = student
                db.close()
                print("Record updated.")
            elif updateoption == '6':
                print("Update record cancelled.")
                clearscreen()
                break
            else:
                print("Invalid input.")
    else:
        print("Student number %s does not exist." % number)

# Checks if number, coursemark and exammark only contain decimal digits
    if number.isdigit() == False:
        number = input('Student number entered contains a letter, please input again: ')
    if coursemark.isdigit() == False:
        coursemark = input('Coursemark entered contains a letter, please input again: ')
    if exammark.isdigit() == False:
        exammark = input('Exammark entered contains a letter, please input again: ')
# Checks if title, forename and surname only contain alphabetic characters
    if title.isdigit() == False:
        title = input('Title entered contains a number, please input again: ')
    if forename.isdigit() == False:
        forename = input('Forename entered contains a number, please input again: ')
    if surname.isdigit() == False:
        surname = input('Surname entered contains a number, please input again: ')
# Checks if module contains two upper case characters followed by four decimal digits
    if module[0:1].islower() == True or module[2:5].isalpha() == True:
        module = input('Module must be inputted in the format of two uppercase letters followed by four decimal digits, please input again: ')

def deleterecord():
# Deletes a record from the database
# Prompts user for the student number and module
    number = input('Please select student number: ')
    module = input('Please select student module: ')
# Checks if number only contains decimal digits
    if number.isdigit() == False:
        number = input('Student number entered contains a letter, please input again: ')    
# Checks if module contains two upper case characters followed by four decimal digits
    if module[0:1].islower() == True or module[2:5].isalpha() == True:
        module = input('Module must be inputted in the format of two uppercase letters followed by four decimal digits, please input again: ')    
    db = shelve.open(module)
    if number in db:
        value = db[number]
        print(value)
        while True:
            confirmdelete = input('Do you wish to delete this record, Y/N?: ')
            if confirmdelete == 'Y' or 'y' or 'Yes' or 'YES':
                # Delete record
                del db[number]
                print("Record deleted.")
                break
            elif confirmdelete == 'N' or 'n' or 'No' or 'NO':
                print("Record not deleted.")
                break
            else:
                print("Please confirm you wish to delete this record.")
                continue
    db.close()

def displayall():
# Displays a list of all the students in the database
    module = input('To display student records, please select a module: ')
    db = shelve.open(module)
    for number in db:
        student = db[number]
        student_info = student.split(' ')
        title = student_info[1]
        forename = student_info[2]
        surname = student_info[3]
        coursemark = student_info[5]
        exammark = student_info[6]
        print("""
            List of students on module %s""" % module)
        print("""
            Name                        Mark
            %s         %2d""" % (title + ' ' + forename + ' ' + surname, int(coursemark) + int(exammark)))
    db.close()

# MENU INTERFACE
while True:
    menuoption = input("""    
             Module Records

        (1) Add a record
        (2) Display a record
        (3) Update a record
        (4) Delete a record
        (5) Display the details of all students on the module
        (6) Exit

           Select option:- """)
    if menuoption == '1':
        clearscreen()
        print("Add record")
        addrecord()
    elif menuoption == '2':
        clearscreen()
        print("Record")
        displayrecord()
    elif menuoption == '3':
        clearscreen()
        print("Update record")
        updaterecord()
    elif menuoption == '4':
        clearscreen()
        print("Delete record")
        deleterecord()
    elif menuoption == '5':
        clearscreen()
        print("Display all records")
        displayall()
    elif menuoption == '6':
        clearscreen()
        break
    else:
        print("Invalid input.")
print("Menu closed.")