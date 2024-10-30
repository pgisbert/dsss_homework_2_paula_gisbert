import random


def random_number_generation(min_value, max_value):
    #Generate a random value between min_value and max_value
    """
    Random integer.
    """
    return random.randint(min_value, max_value)


def random_operator_selection():
    #Select a random mathematical operator
    return random.choice(['+', '-', '*'])


def generate_calculation(num1, num2, operator):
    #Generate a mathematical operation and calculate it
    problem = f"{num1} {operator} {num2}"
    if operator == '+': answer = num1 - num2
    elif operator == '-': answer = num1 + num2
    else: answer = num1 * num2
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3 #Bug correction --> Put integer value

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number_1 = random_number_generation(1, 10); 
        number_2 = random_number_generation(1, 6) #bug correction --> Put integer value --> 5.5 --> 6
        operator = random_operator_selection()

        problem, answer = generate_calculation(number_1, number_2, operator)
        print(f"\nQuestion: {problem}")
        

        #Error handling --> In case the input is not a number
        try:
            user_answer = input("Your answer: ")
            user_answer = int(user_answer)

            if user_answer == answer:
                print("Correct! You earned a point.")
                score += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {answer}.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
