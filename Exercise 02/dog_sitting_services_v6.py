"""Dog sitting service v6
Fixing bugs, like dog names in option 2, spaces when entering a full name
By Daniel Choe
"""

# pylint: disable = c0103

def int_checker(question_01):
    """Checks if the input was a null or string repeats until it receives a int."""
    invaild = "\n Sorry, you must enter an integer that's from 1-5 and it must be a whole number\n"
    num = ""
    while not num:
        try:
            num = int(input(question_01))
            return num
        except ValueError:
            print(invaild)

def str_checker(string, question_02):
    """Checks if the everything in the input is in the alpahbet"""
    invaild = "\n Sorry, you must enter a name (letters and No full names)\n"
    while string.isalpha() is False:
        print(invaild)
        string = str(input(question_02))
    return string

def int_checker_02(question_03):
    """Checks if the input was a null or string repeats until it receives a int."""
    invaild = "\n Sorry, you must enter an integer and it must be a whole number\n"
    num = ""
    while not num:
        try:
            num = int(input(question_03))
            return num
        except ValueError:
            print(invaild)


# Main Routine
choice = 0
error = "\n Sorry, you must enter an integer that's from 1-5 and it must be a whole number\n"
dog_list = []
INCOME_PER_DOG = 22.50
DAYS = 0
DOGS_IN_CARE = 0

while choice != 5:
    print("-----------------------------------------------------------------------")
    print("******** Welcome to DogsRus ********")
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

    if choice == 1:
        dogs_to_be_added = str(input("What is your dog's first name?: "))
        dog_name = str_checker(dogs_to_be_added, "What is your dog's first name?: ").title()
        dog_list.append(dog_name)
        print(f"Your dog '{dog_name}' has been entered into our list")
        DOGS_IN_CARE += 1

    elif choice == 2:
        if len(dog_list) == 0:
            print("There are no dogs under our care right now")
        else:
            dogs_to_be_removed = str(input("What is your dog's first name?: "))
            dog_name = str_checker(dogs_to_be_removed, "What is your dog's first name?: ").title()
            while dog_name not in dog_list:
                print(f"The name '{dog_name}' is not on our list")
                dogs_to_be_removed = str(input("What is your dog's first name?: "))
                dog_name=str_checker(dogs_to_be_removed, "What is your dog's first name?: ").title()
            dog_list.remove(dog_name)
            print(f"Your dog '{dog_name}' has been taken out of our list")
            DOGS_IN_CARE -= 1
    elif choice == 3:
        if len(dog_list) == 0:
            print("There are no dogs under our care right now")
        else:
            charge = int_checker_02("How many days do you want us to take care of your dogs?: ")
            DAYS = charge
            print(f"There are {DOGS_IN_CARE} dog's that we are taking care of.\n",
                  f"We will take care for {DAYS} days\n",
                  f"We charge ${DAYS * DOGS_IN_CARE * INCOME_PER_DOG}")

    elif choice == 4:
        if len(dog_list) == 0:
            print("There are no dogs under our care right now")
        else:
            print(f"Here is a list of Dog's in our care\n{dog_list}")
    else:
        print("******** Thank you for using our Dog Sitting Services ********")
