# Вариант программы для строго 4 чисел (2 автобусов)
# Ввод четырех чисел - получаем список, передаем лямбда функции-1
# лямбда функция-1: складываем отсортированные срезы списка и передаем л.ф.-2
# лямбда функция-2: выбираем максимальное число между "нулем"
# и "разницей минимального из правых концов отрезков и максимального из левых концов отрезков + 1"
# Результат выводим в консоль

if __name__ == '__main__':
    print((lambda b: max(0, min(b[1], b[3]) - max(b[0], b[2]) + 1))
          ((lambda c: sorted(c[0:1+1]) + sorted(c[2:3+1]))
           (list(map(int, input().split())))))
