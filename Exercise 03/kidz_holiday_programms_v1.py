"""Kidz holiday programme
User is asked to input the name of the holiday programme which the child is attending.
By Daniel
"""
# pylint: disable = c0103

def str_checker(string, question_01):
    """Checks if the everything in the input is in the alpahbet"""
    invaild = "\nSorry, you must enter F,A or X\n"
    while string.isalpha() is False:
        print(invaild)
        string = str(input(question_01))
    return string


#Main Routine
keep_running = True
ERROR = "\nSorry, you must enter F,A or X\n"
while keep_running:
    repeat = "No"
    print("-----------------------------------------------------------------------")
    print("******** Welcome to Holiday Kidz Programme! ********")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()
    print("F = Sign your child up for 'Fun in the sun'")
    print("A = Sign your child up for 'Active Kidz'")
    print("'X' = End and List of children and their age in each programme")
    print()
    choice = input("Enter your choice (enter F,A or X): ")
    choice_check = str_checker(choice, "Enter your choice (enter F,A or X): ").title()

    if choice_check == "X":
        keep_running = False

    while repeat != "Go":
        if choice_check == "F":
            print(f"{choice_check}")
            repeat = "Go"
        elif choice_check == "A":
            print(f"{choice_check}")
            repeat = "Go"
        else:
            print(ERROR)
            choice = input("Enter your choice (enter F,A or X): ")
            choice_check = str_checker(choice, "Enter your choice (enter F,A or X): ").title()
