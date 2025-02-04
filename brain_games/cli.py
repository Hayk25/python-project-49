import prompt

def welcome_user():
    """Запрашивает имя у пользователя и выводит приветствие."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')



welcome_user()