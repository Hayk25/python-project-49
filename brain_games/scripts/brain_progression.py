import random

from brain_games.cli import welcome_user


def is_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answer_count = 0

    for i in range(3):
        random_int = random.randint(1, 100)
        print(f'Question: {random_int}')

        answer = input("Your answer: ").strip().lower()

        if answer not in ["yes", "no"]:
            print(
                f"'{answer}' is an incorrect input. "
                f"The correct answer was "
                f"'{'yes' if random_int % 2 == 0 else 'no'}'.")
            print(f"Let's try again, {name}!")
            return

        correct_answer = "yes" if random_int % 2 == 0 else "no"

        if answer == correct_answer:
            print("Correct!")
            correct_answer_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    if correct_answer_count == 3:
        print(f"Congratulations, {name}!")


def main():
    is_even()


if __name__ == '__main__':
    main()
