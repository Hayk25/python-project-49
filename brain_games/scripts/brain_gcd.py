import math
import random

from brain_games.cli import welcome_user


def gcd_game():
    name = welcome_user()
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
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_gcd}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    gcd_game()


if __name__ == '__main__':
    main()
