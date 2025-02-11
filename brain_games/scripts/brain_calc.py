import random


def calculation():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    correct_answers = 0  # Количество правильных ответов

    while correct_answers < 3:
        # Генерируем выражение
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operator = random.choice(["+", "-", "*"])
        expression = f"{num1} {operator} {num2}"
        correct_result = str(eval(expression))  # Вычисляем правильный ответ

        print(f"Question: {expression}")
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_result:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_result}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при ошибке

    print(f"Congratulations, {name}!")  # Если 3 правильных ответа подряд


calculation()
