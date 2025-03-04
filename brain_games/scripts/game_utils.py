import prompt

ROUND_LIMIT = 3


def ask_question(question):
    print(question)
    answer = prompt.string('Your answer: ')
    return answer


def compare_answer(answer, result):
    return str(answer).strip() == str(result).strip()
