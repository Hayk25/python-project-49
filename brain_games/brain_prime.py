import random

def is_prime(num):

    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def brain_prime():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer \"yes\" if the number is prime. Otherwise answer \"no\".")

    correct_answer_count = 0  # Количество правильных ответов

    while correct_answer_count < 3:
        random_int = random.randint(1, 100)  # Генерируем случайное число
        print(f"Question: {random_int}")

        answer = input("Your answer: ").strip().lower()

        # Проверяем правильность ответа
        correct_answer = "yes" if is_prime(random_int) else "no"

        if answer not in ["yes", "no"]:
            print(f"'{answer}' is an incorrect input. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при некорректном вводе

        if answer == correct_answer:
            print("Correct!")
            correct_answer_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при ошибке

    print(f"Congratulations, {name}!")  # Если 3 правильных ответа подряд

brain_prime()
