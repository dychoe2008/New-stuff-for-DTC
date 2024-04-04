"""Dog sitting service
Ask if the user wants to pick a dog up, it should ask for the dog's name and remove it from the list.
If the name is not there it should say that
By Daniel Choe
"""

def int_checker(question_01):
    """Checks if the input was a null or string repeats until it receives a int."""
    error = "\n Sorry, you must enter an integer that's from 1-5 and it must be a whole number\n"
    num = ""
    while not num:
        try:
            num = int(input(question_01))
            return num
        except ValueError:
            print(error)

def str_checker(string, question):
    """Checks if the everything in the input is in the alpahbet"""
    error = "\n Sorry, you must enter a name (letters)\n"
    while string.isalpha() is False:
        print(error)
        string = str(input(question))
    return string

# Main Routine
choice = 0
dog_list = []
error = "\n Sorry, you must enter an integer that's from 1-5 and it must be a whole number\n"
while choice != 5: 
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
    choice = int_checker("Enter your choice (number between 1 and 5): ")
    while choice < 1 or choice > 5:
        print(error)
        choice = int_checker("Enter your choice (number between 1 and 5): ")
    print()

    if choice==1:
        dogs_to_be_added = str(input("What is your dog's name?: "))
        dog_name = str_checker(dogs_to_be_added, "What is your dog's name?: ")
        dog_list.append(dog_name)
        print(dog_list)

    elif choice==2:
        dogs_to_be_removed = str(input("What is your dog's name?: "))
        dog_name = str_checker(dogs_to_be_removed, "What is your dog's name?: ")
        while dog_name not in dog_list:
            print("The name of this dog is not on our list")
            dogs_to_be_removed = str(input("What is your dog's name?: "))
            dog_name = str_checker(dogs_to_be_removed, "What is your dog's name?: ")
        dog_list.remove(dog_name)
        print(f"Your dog {dog_name} has been taken out of our list")

    elif choice==3:
        calcCost()
    elif choice==4:
        printRoll()
    else:
        quit()
