# SummativeTask1 - Math Quiz Program

# Task 2: User Manual and Technical Documentation for Task 1

## **User Manual**

Welcome to the Math Quiz Program! This program is designed to test and improve your mathematical problem-solving skills. You will solve simple multiplication equations and receive immediate feedback on your answers. No prior knowledge of programming in python is required to use this program. Follow the instructions below to install and run the program successfully.

This program offers an engaging way to practice multiplication and develop quick mental calculation skills. Each round of the quiz challenges users to solve equations accurately, promoting fun learning. At the end of each round, you will see your final score, giving a clear view of your performance.

---
### System Requirements
- **Operating System**: macOS, Windows, or Linux.
- **Python Version**: Python 3.9 or higher installed on your system.
- **Software**: Visual Studio Code (VS Code) is used in development and is recommended as the code editor.

---
### Installation Instructions
Follow the below steps to set up the Math Quiz Program
1. Install Python
  - Download Python 3.9 or higher from [https://www.python.org/](https://www.python.org/).
  - Follow the instructions to install Python on your system.
  - Confirm the installation by opening a terminal annd typing:
  ```python3 --version```

2. Install Visual Studio Code:
  - Download and install VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/).
  - Install the Python extension for VS Code.

3. Download Program Files:
  - Save the program code into a file named `main.py`.
  - Store this file in a dedicated folder for the Math Quiz Program

4. Set up the Environment:
  - Open Visual Studio Code
  - Use `File > Open Folder` to select the folder containing `main.py`.

---
### Running the Program
To start the Math Quiz:
  1. Open VS Code
  2. Open the terminal in VS Code by selecting`View > Terminal`from the menu.
  3. In the terminal, run the program and follow the on-screen prompts to solve the equations.

For each question, type your answer when prompted. The program will provide immediate feedback on whether the answer was correct.

---
### Example Interaction
Here’s an example of how the program works:
- **Question (Program output)**: Solve the equation: 3 * x = 12
- **Answer (User Input)**: 4
- **Feedback**: "Well done, right answer!"

The process repeats for five questions. At the end, the program displays your total score, such as:
- "Quiz over. Your final score is 4/5"
---
### Troubleshooting
Here are solutions to common problems:
- Error: “Command not found” when running the program.
  - Ensure Python is installed and added to your system path.
- Error: “Invalid input” message when answering a question.
  - Enter only numeric values. Non-numeric values are not accepted.
- Program does not run:
  - Confirm that the filename is correct (`main.py`)
---
## Technical Documentation
### Overview
The Math Quiz Program is a Python script that generates random multiplication equations, prompts the user to solve for `x`, and tracks their score. The script showcases basic programming concepts, including functions, loops, conditional statements and input validation.

---
### Code Components:
Functions:
- `random`: Generates random numbers for the equations.
- `generate_equation()`: This function generates a random multiplier (`a`), a solution (`x`), and computes the product (`b`) in the form `a * x = b`.
- `ask_question(a,b)`: Displays an equation, gets the user's answer and ensures valid numeric input from the user.
- `check_answer(user_name, correct_answer)`: Validates the user's input against the correct answer.
- `math_quiz()`: Runs the overall quiz and manages the quiz loop.

Flow:
- The program initialises a score counter and loops through five questions.
- For each question, it generates a random question, prompts the user, checks their answer, and updates the score.
- At the end, the program displays the user's final score.

---
### Error Handling:
- Input errors are managed using `try` and `except` blocks to ensure only valid numbers are accepted.
- Invalid input prompts the user to re-enter their answer.

Example:
```
try:
    user_answer = int(input("What is x? "))
except ValueError:
    print("Invalid input. Please enter a number.")
```
---
### The program has been tested for:

1. Valid Input:
- Equation: `3 * x = 12`
- User Input: `4`
- Output: "Well done, right answer!"

2. Invalid Input:
- Input: `abc`
- Output: "Invalid input. Please enter a number."

### Version Information
This program was develop using Python 3.12.4. Ensure compatibiltity by using Python 3.9 or higher.
