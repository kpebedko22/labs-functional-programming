
import random
import string
import itertools
from collections import Counter


def task_1():

    def leapfrog(integers: list, strings: list):
        """
        Функция объединения двух списков в один с чередованием элемнтов
        """
        return list(filter(None, sum(itertools.zip_longest(integers, strings), ())))

    # Генерируем рандомное число - размер списка натуральных чисел
    # Заполняем список натуральных чисел
    size = random.randint(2, 10)
    integers = list(i for i in range(1, size + 1))

    # Генерируем рандомное число - размер списка строк
    # letters - латинские буквы нижнего регистра
    # Заполняем список строк
    size = random.randint(2, 10)
    letters = string.ascii_lowercase
    strings = list(map(
        lambda length: ''.join(random.choice(letters) for _ in range(length)),
        [random.randint(2, 10) for _ in range(size)]
    ))

    # Выводим списки
    print('Список натуральных чисел: \r\n{}\r\n'.format(integers))
    print('Список строк: \r\n{}\r\n'.format(strings))

    # Создаем и выводим список длин подстрок
    lengths = list(map(lambda x: len(x), strings))
    print('Список длин подстрок из списка строк: \r\n{}\r\n'.format(lengths))

    # То же самое, но словарь
    dictionary = {x: len(x) for x in strings}
    print('Словарь подстрок и их длин: \r\n{}\r\n'.format(dictionary))

    # Объединяем списки
    res = leapfrog(integers, strings)

    # Выводим объединение списков
    print('Список с чередованием элементов: \r\n{}\r\n'.format(res))


def task_2_1():
    def sorting(data: list):
        lengths = list(map(lambda x: len(x), data))

        result = [item for items, c in Counter(
            lengths).most_common() for item in [items] * c]
        result.reverse()

        res = []
        while len(data):
            for x in result:
                for i in data:
                    if len(i) == x:
                        res.append(i)
                        data.remove(i)
                        break
        return res

    # Генерируем рандомное число - размер списка списков
    # Заполняем список списками чисел разного размера
    size = random.randint(7, 10)
    list_of_lists = [
        [random.randint(1, 10) for _ in range(random.randint(1, 6))] for _ in range(size)
    ]
    print('Список списков: \r\n{}\r\n'.format(list_of_lists))
    sorted_lists = sorting(list_of_lists)
    print('Отсортированный по частотности: \r\n{}\r\n'.format(sorted_lists))


def task_2_2():
    def factorization(n: int):
        simples = []
        d = 2

        while d * d <= n:
            if n % d == 0:
                simples.append(d)
                n //= d
            else:
                d += 1

        if n > 1:
            simples.append(n)

        return simples

    num = random.randint(1, 2015)
    res = factorization(num)
    print('Разложение числа на простые множители: \r\n{} = {}\r\n'.format(num, res))


if __name__ == '__main__':
    task_1()

    task_2_1()

    task_2_2()
