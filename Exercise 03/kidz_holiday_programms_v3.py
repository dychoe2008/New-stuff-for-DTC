"""Kidz holiday programme v3
For each holiday programme, keeps a record of the number of children who attended the program 
and a total (count/total) of their ages.
By Daniel
"""
# pylint: disable = c0103
def str_checker(string, question_01):
    """Checks if the everything in the input is in the alpahbet"""
    invaild = "\n Sorry, you must enter F,A or X\n"
    while string.isalpha() is False:
        print(invaild)
        string = str(input(question_01))
    return string

def int_checker(question_02):
    """Checks if the input was a null or string repeats until it receives a int."""
    invaild = "\n Sorry, you must enter an integer that's 5-15 and it must be a whole number\n"
    num = ""
    while not num:
        try:
            num = int(input(question_02))
            return num
        except ValueError:
            print(invaild)

#Main Routine
ERROR_01 = "\n Sorry, you must enter F,A or X\n"
ERROR_02 = "\n Sorry, you must enter an age from 5-15\n"
keep_running = True
child_age_list = []

while keep_running:
    repeat = "Go"
    print("-----------------------------------------------------------------------")
    print("******** Welcome to Holiday Kidz Programme! ********")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()
    print("F = Sign your child up for 'Fun in the sun'")
    print("A = Sign your child up for 'Active Kidz'")
    print("X = End and List of children and their age in each programme")
    print()
    choice = input("Enter your choice (enter F,A or X): ")
    choice_check = str_checker(choice, "Enter your choice (enter F,A or X): ").title()

    while repeat != "Stop":
        if choice_check == "X":
            repeat = "Stop"
            keep_running = False
            print(child_age_list)
        elif choice_check == "F":
            repeat = "Stop"
            child_age = int_checker("Enter your childs age (5-15 only): ")
            while child_age < 5 or child_age > 15:
                print(ERROR_02)
                child_age = int_checker("Enter your childs age (5-15 only): ")
            child_age_list.append(child_age)
        elif choice_check == "A":
            repeat = "Stop"
            child_age = int_checker("Enter your childs age: ")
            while child_age < 5 or child_age > 15:
                print(ERROR_02)
                child_age = int_checker("Enter your childs age: ")
            child_age_list.append(child_age)
        else:
            print(ERROR_01)
            choice = input("Enter your choice (enter F,A or X): ")
            choice_check = str_checker(choice, "Enter your choice (enter F,A or X): ").title()
