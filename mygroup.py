# Лабораторная работа №1. Студент: Уткин С. А., группа БСТ2354
import sys

groupmates = [
    {
        "name": "Сергей",
        "surname": "Уткин",
        "exams": ["Информатика", "Базы данных", "Web"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Алина",
        "surname": "Бестаева",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 3]
    },
    {
        "name": "Давид",
        "surname": "Кесаев",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Мадина",
        "surname": "Дзуцева",
        "exams": ["Информатика", "ОС", "Web"],
        "marks": [3, 4, 3]
    },
    {
        "name": "Тимур",
        "surname": "Цаллаев",
        "exams": ["Базы данных", "ОС", "Python"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Залина",
        "surname": "Хадонова",
        "exams": ["Философия", "АиГ", "Python"],
        "marks": [3, 3, 4]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(40), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10),
              str(student["exams"]).ljust(40), str(student["marks"]).ljust(20))


def average(marks):
    return sum(marks) / len(marks)


def filter_students(students, min_avg):
    """Возвращает студентов, средний балл которых выше заданного."""
    return [s for s in students if average(s["marks"]) > min_avg]


if __name__ == "__main__":
    print("Все студенты:")
    print_students(groupmates)
    print()
    while True:
        try:
            raw = input("Введите средний балл для фильтрации: ")
            if not sys.stdin.isatty():
                print(raw)  # при вводе через конвейер (echo 4| python mygroup.py) показываем введённое значение
            min_avg = float(raw.replace(",", "."))
            break
        except ValueError:
            print("Ошибка: нужно ввести число, например 4 или 4.5")
    result = filter_students(groupmates, min_avg)
    print()
    if result:
        print("Студенты со средним баллом выше", min_avg, ":")
        print_students(result)
    else:
        print("Нет студентов со средним баллом выше", min_avg)
