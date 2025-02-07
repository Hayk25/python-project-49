import random

def is_even():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answer_count = 0

    for i in range(3):
        random_int = random.randint(1, 100)
        print(f'Question: {random_int}')

        answer = input("Your answer: ").strip().lower()


        if answer not in ["yes", "no"]:
            print(f"'{answer}' is an incorrect input. Correct answer was '{'yes' if random_int % 2 == 0 else 'no'}'.")
            print(f"Let's try again, {name}!")
            return

        correct_answer = "yes" if random_int % 2 == 0 else "no"

        if answer == correct_answer:
            print("Correct!")
            correct_answer_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    if correct_answer_count == 3:
        print(f"Congratulations, {name}!")


is_even()
