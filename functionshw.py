#Write a program that validates input values using just one function. 
#Ask the user to enter hours and minutes and the program should use one function to validate if the hours are between 
#0 and 23 and the minutes are between 0 and 59. Program output should indicate the number of hours and minutes and 
#the input validation function should keep asking the user to enter valid values.This one input validation function 
#should be called from the main function.
#See sample output below. Submit python program and screenshot of output



def validate_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Value must be between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    hours = validate_input("Enter hours (0-23): ", 0, 23)
    minutes = validate_input("Enter minutes (0-59): ", 0, 59)
    print(f"Valid time entered: {hours} hours and {minutes} minutes")

if __name__ == "__main__":
    main()

input('press enter to close program')    
