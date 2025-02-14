import random

from brain_games.cli import welcome_user


def is_prime(num):
    """Простая проверка на простое число"""
    if num < 2:
        return False
    for i in range(2, num):  # Проверяем все числа от 2 до num-1
        if num % i == 0:
            return False
    return True


def brain_prime():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is prime. Otherwise answer "no".')

    correct_answers = 0

    while correct_answers < 3:
        num = random.randint(1, 50)  # Генерируем число от 1 до 50
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
            return  # Завершаем игру при ошибке

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    brain_prime()
