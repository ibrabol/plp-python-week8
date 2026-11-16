
# Personal Mini-Toolkit

## Project Description

The Personal Mini-Toolkit is a menu-driven Python application developed
for the PLP Python Week 8 Final Project.

It provides three useful tools:
- Even or Odd Checker: Determines whether a number is even or odd.
- Simple Calculator: Performs addition, subtraction, multiplication, and division.
- Number List Manager: Allows users to add, view, calculate the total,
  and remove numbers from a list.

The program uses loops, conditionals, lists, functions, variables,
input/output, and exception handling.

## How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

   python toolkit.py

6. Select a tool from the menu.
7. Choose Quit when you want to exit.

## Project Files

- toolkit_plan.txt: Contains the project planning document.
- toolkit.py: Contains the complete Python application.
- screenshots/: Contains screenshots showing the menu and tools.

## Testing

The program was tested with:
- Valid menu selections.
- Invalid menu selections.
- Even and odd numbers.
- Calculator operations.
- Division by zero.
- Adding and removing numbers.
- Empty lists.
- Returning to the menu.
- Quitting the program.

## Reflection

The hardest part of this project was organizing the tools into
functions and making the menu return after each tool finished.
The list manager required careful handling because numbers could
be added and removed while the program was running.
The longest bug to fix was making sure invalid inputs did not
crash the calculator or list manager.
Using try and except helped the program handle incorrect inputs
gracefully.
I also learned how loops and conditionals work together to make
a menu-driven application.
If I had one more week, I would add a password generator and
a tool that saves list data to a file.
This project improved my confidence in writing structured Python
programs.
