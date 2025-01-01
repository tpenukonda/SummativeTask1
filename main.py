import random

def generate_equation():
    """Generates a random equation in the form 'a * x = b'."""
    a = random.randint(1, 10)
    x = random.randint(1, 10)
    b = a * x
    return a, x, b

def ask_question(a, b):
    """Displays the question and gets the user's answer."""
    while True:
         try:
              print(f"Solve the equation: {a} * x = {b}")
              user_answer = int(input("What is x? "))
              return user_answer
         except ValueError:
              print("Invalid input. Please enter a number.")

def check_answer(user_answer, correct_answer):
    """Checks if the user's answer is correct."""
    if user_answer == correct_answer:
        print("Well done, right answer!")
        return True
    else:
        print(f"Incorrect answer. The correct answer is {correct_answer}.")
        return False

def math_quiz():
    """Runs the math quiz."""
    score = 0
    num_questions = 5

    for i in range(num_questions):
        #Display the question number
        print(f"\nQuestion {i + 1}/{num_questions}")

        # Generate a new equation
        a, x, b = generate_equation()

        # Ask the question and get the user's anser
        user_answer = ask_question(a, b)

        # Check if the user's answer is correct
        if check_answer(user_answer, x):
            score +=1

    #Display the final score after all questions
    print(f"Quiz Over. Your final score is {score}/{num_questions}.")

if __name__ == "__main__":
            print("Welcome to the Math Quiz!")
            math_quiz()