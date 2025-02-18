import random

from brain_games.cli import welcome_user


def progression_game():
    name = welcome_user()
    print("What number is missing in the progression?")

    correct_answers = 0  # Количество правильных ответов

    while correct_answers < 3:
        start = random.randint(1, 10)  # Начальное число
        step = random.randint(2, 5)  # Шаг прогрессии
        progression = [start + i * step for i in range(10)]  # Создаём 10 элементов
        hidden_index = random.randint(0, 9)  # Индекс скрытого числа
        correct_answer = str(progression[hidden_index])  # Запоминаем правильный ответ
        progression[hidden_index] = ".."  # Заменяем число на ".."

        print("Question:", " ".join(map(str, progression)))
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при ошибке

    print(f"Congratulations, {name}!")  # Если 3 правильных ответа подряд


def main():
    progression_game()


if __name__ == '__main__':
    main()
