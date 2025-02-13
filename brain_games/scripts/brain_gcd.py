import random
import math


def gcd_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    correct_answers = 0

    while correct_answers < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)


        correct_gcd = str(math.gcd(num1, num2))

        print(f"Question: {num1} {num2}")
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_gcd:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_gcd}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


gcd_game()
