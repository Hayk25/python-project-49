import random

from brain_games.cli import welcome_user


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def brain_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers = 0

    while correct_answers < 3:
        num = random.randint(1, 50)
        print(f"Question: {num}")
        answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if is_prime(num) else "no"

        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    brain_prime()


if __name__ == '__main__':
    main()
