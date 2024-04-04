"""Dog sitting service
Print the welcome screen and ask the user for an input from 1-5
By Daniel Choe
"""

def int_checker(question):
    """Checks if the input was a null or string repeats until it receives a int."""
    error = "\n Sorry, you must enter an integer that's from 1-5\n"
    num = ""
    while not num:
        try:
            num = int(input(question))
            return num
        except ValueError:
            print(error)



# Main Routine
print("-----------------------------------------------------------------------")
print("Welcome to DogsRus")
print("What would you like to do? Please choose one of the items below")
print("-----------------------------------------------------------------------")
print()
print("1 = Drop off a dog")
print("2 = Pick up a dog")
print("3 = Calculate cost")
print("4 = Print roll")
print("5 = Exit the system")
print()
choice=int_checker("Enter your choice (number between 1 and 5): ")
print()





