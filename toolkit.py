
# Personal Mini-Toolkit
# PLP Python Week 8 Final Project

# Tool 1: Check whether a number is even or odd.
def even_odd_checker():
    print("\n--- Even or Odd Checker ---")

    try:
        number = int(input("Enter a whole number: "))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    except ValueError:
        print("Please enter a valid whole number.")


# Tool 2: Perform basic mathematical calculations.
def simple_calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your operation (1-4): ")

        if operation == "1":
            result = first_number + second_number
            print(f"Result: {first_number} + {second_number} = {result}")

        elif operation == "2":
            result = first_number - second_number
            print(f"Result: {first_number} - {second_number} = {result}")

        elif operation == "3":
            result = first_number * second_number
            print(f"Result: {first_number} * {second_number} = {result}")

        elif operation == "4":
            if second_number == 0:
                print("Sorry, division by zero is not allowed.")
            else:
                result = first_number / second_number
                print(f"Result: {first_number} / {second_number} = {result}")

        else:
            print("Invalid operation. Please choose 1, 2, 3, or 4.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")


# Tool 3: Manage a list of numbers.
def number_list_manager():
    print("\n--- Number List Manager ---")

    numbers = []

    while True:
        print("\nList Manager Menu")
        print("1. Add a number")
        print("2. View numbers")
        print("3. Calculate total")
        print("4. Remove a number")
        print("5. Return to main menu")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            try:
                number = float(input("Enter a number to add: "))
                numbers.append(number)
                print(f"{number} has been added successfully.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            if len(numbers) == 0:
                print("Your list is currently empty.")
            else:
                print("Your numbers are:")
                for number in numbers:
                    print(f"- {number}")

        elif choice == "3":
            total = sum(numbers)
            print(f"The total of your numbers is {total}.")

        elif choice == "4":
            if len(numbers) == 0:
                print("There are no numbers to remove.")
            else:
                try:
                    number = float(input("Enter the number to remove: "))

                    if number in numbers:
                        numbers.remove(number)
                        print(f"{number} has been removed.")
                    else:
                        print(f"{number} was not found in your list.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


# Main program: Display the menu and handle user choices.
def main():
    print("=" * 40)
    print("WELCOME TO YOUR PERSONAL MINI-TOOLKIT!")
    print("Your collection of useful Python tools.")
    print("=" * 40)

    while True:
        print("\nMAIN MENU")
        print("1. Even or Odd Checker")
        print("2. Simple Calculator")
        print("3. Number List Manager")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            even_odd_checker()

        elif choice == "2":
            simple_calculator()

        elif choice == "3":
            number_list_manager()

        elif choice == "4":
            print("\nThank you for using the Personal Mini-Toolkit!")
            print("Goodbye! Have a wonderful day.")
            break

        else:
            print(f"'{choice}' is not a valid choice.")
            print("Please select an option from 1 to 4.")


# Start the program.
if __name__ == "__main__":
    main()


