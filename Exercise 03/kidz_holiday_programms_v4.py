"""Kidz holiday programme v4
Once the user enters "X" the program then displays the total number 
and average age of the children in each holiday programme.
By Daniel
"""
# pylint: disable = c0103
def str_check(string, question_01):
    """Checks if the everything in the input is in the alpahbet"""
    invaild = "\n Sorry, you must enter F,A or X\n"
    while string.isalpha() is False:
        print(invaild)
        string = str(input(question_01))
    return string

def int_checker(question_02):
    """Checks the input was a null or string repeats until receives a int."""
    invaild = "\n You must enter an integer that's 5-15\n"
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
C_A_list_F = []
total_C_F = 0
C_A_list_A = []
total_C_A = 0

while keep_running:
    repeat = "Go"
    print("------------------------------------------------------------------")
    print("******** Welcome to Holiday Kidz Programme! ********")
    print("What would you like to do? Please choose one of the items below")
    print("------------------------------------------------------------------")
    print()
    print("F = Sign your child up for 'Fun in the sun'")
    print("A = Sign your child up for 'Active Kidz'")
    print("X = End and List of children and their age in each programme")
    print()
    choice = input("Enter your choice (F,A or X): ")
    choice_c = str_check(choice, "Enter your choice (F,A or X): ").title()

    while repeat != "Stop":
        if choice_c == "X":
            repeat = "Stop"
            keep_running = False
            total_C_F = len(C_A_list_F)
            total_C_A = len(C_A_list_A)

            if total_C_F == 0 and total_C_A == 0:
                print("We have no children signed up for either activities")
            elif total_C_F == 0:
                a_A_A = sum(C_A_list_A) // len(C_A_list_A)
                print("We have no children signed up for 'Fun in the Sun'")
                print(f"A:\nChildren = {total_C_A}\nAverage = {round(a_A_A)}")
            elif total_C_A == 0:
                a_A_F = sum(C_A_list_F) // len(C_A_list_F)
                print("We have no children signed up for 'Active Kidz'")
                print(f"F:\nChildren = {total_C_F}\nAverage = {round(a_A_F)}")
            else:
                a_A_F = sum(C_A_list_F) // len(C_A_list_F)
                a_A_A = sum(C_A_list_A) // len(C_A_list_A)
                print(f"F:\nChildren = {total_C_F}\nAverage = {round(a_A_F)}")
                print(f"A:\nChildren = {total_C_A}\nAverage = {round(a_A_A)}")
                print("Thank you for signing up to our programms!")

        elif choice_c == "F":
            repeat = "Stop"
            child_age = int_checker("Enter the age your child (5-15 only): ")
            while child_age < 5 or child_age > 15:
                print(ERROR_02)
                child_age=int_checker("Enter the age your child (5-15 only): ")
            C_A_list_F.append(child_age)
        elif choice_c == "A":
            repeat = "Stop"
            child_age = int_checker("Enter the age your child (5-15 only): ")
            while child_age < 5 or child_age > 15:
                print(ERROR_02)
                child_age=int_checker("Enter the age your child (5-15 only): ")
            C_A_list_A.append(child_age)
        else:
            print(ERROR_01)
            choice = input("Enter your choice (F,A or X): ")
            choice_c=str_check(choice,"Enter your choice (F,A or X): ").title()
