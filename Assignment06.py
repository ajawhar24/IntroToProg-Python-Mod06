# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Abdullah Jawhar>,<02/23/2024>,<Assignment06>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# - File Processing - #

class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str, student_data:list):
        '''
        Reads data from file

        '''
        try:
            file = open(file_name,"r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        '''
        Writes data to file

        '''
        try:
            file = open(FILE_NAME, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with writing to the file.", e)
        finally:
            if file.closed == False:
                file.close()

# - IO Processing - #
class IOProcessor:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        ''' This displays a custom error message to the user

        '''
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')
    @staticmethod
    def output_menu(menu:str):
        ''' This displays the menu of choices to the user

        '''
        print(menu)
    @staticmethod
    def input_menu_choice():
        '''This recieves menu choice from user

        '''
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please only choose 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice
    @staticmethod
    def input_student_info(student_data: list):
        '''This recieves students registration information from user
        '''
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("One of the values entered was not the right type", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)
        return student_data
    @staticmethod
    def output_student_info(student_data: list):
        '''This displays student registration information

        '''
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)


# - Code - #
students = FileProcessor.read_data_from_file(file_name= FILE_NAME, student_data=students)

while (True):

    # Present the menu of choices
    IOProcessor.output_menu(menu=MENU)
    menu_choice = IOProcessor.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        students = IOProcessor.input_student_info(student_data = students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IOProcessor.output_student_info(student_data = students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name = FILE_NAME, student_data = students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")