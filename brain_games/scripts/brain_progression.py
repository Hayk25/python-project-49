import random

from brain_games.cli import welcome_user


def progression_game():
    name = welcome_user()
    print("What number is missing in the progression?")

    correct_answers = 0

    while correct_answers < 3:
        start = random.randint(1, 10)
        step = random.randint(2, 5)
        progression = [start + i * step for i in range(10)]
        hidden_index = random.randint(0, 9)
        correct_answer = str(progression[hidden_index])
        progression[hidden_index] = ".."

        print("Question:", " ".join(map(str, progression)))
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    progression_game()


if __name__ == '__main__':
    main()
