"""Kidz holiday programme
User is asked to input the name of the holiday programme which the child is attending.
By Daniel
"""
def int_checker_01(question_01):
    """Checks if the input was a null or string repeats until it receives a int."""
    invaild = "\n Sorry, you must enter an 1 or 2\n"
    num = ""
    while not num:
        try:
            num = int(input(question_01))
            return num
        except ValueError:
            print(invaild)

#Main Routine
choice = 0
error = "\n Sorry, you must enter an 1 or 2\n"
while choice != "X":
    print("-----------------------------------------------------------------------")
    print("******** Welcome to Holiday Kidz Programme! ********")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()
    print("1 = Sign your child up for 'Fun in the sun'")
    print("2 = Sign your child up for 'Active Kidz'")
    print("'X' = End and List of children and their age in each programme")
    print()
    choice = int_checker_01("Enter your choice (number between 1 or 2/or 'X'): ")
    while choice < 1 or choice > 2:
        print(error)
        choice = int_checker_01("Enter your choice (number between 1 or 2/or 'X'): ")
    print()
