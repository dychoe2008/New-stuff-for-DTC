"""Kidz holiday programme
User is asked to input the name of the holiday programme which the child is attending.
By Daniel
"""
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
