def create_matrix(size: int):
    """
    Создание матрицы заданного размера size.
    """

    # Выделение памяти под матрицу
    matrix = [[0] * size for i in range(size)]

    # Заполнение первого и последнего элемента матрицы
    matrix[0][0] = 1
    matrix[size - 1][size - 1] = size**2

    # Заполнение первой строки матрицы
    for j in range(1, size):
        matrix[0][j] = matrix[0][j - 1] + j + 1

    # Заполнение последнего столбца матрицы
    for i in reversed(range(0, size - 1)):
        matrix[i][size - 1] = matrix[i + 1][size - 1] + i - size + 1

    # Заполнение оставшейся части матрицы
    for j in reversed(range(0, size - 1)):
        for i in range(1, size):
            matrix[i][j] = matrix[i - 1][j + 1] - 1

    return matrix


def print_matrix(matrix):
    """
    Вывод матрицы
    """
    for row in matrix:
        for x in row:
            print("{:4d}".format(x), end="")
        print()


def triangles_area(matrix):
    """
    Получение списка площадей треугольников, где 
    первый и второй элементы каждой строки матрицы - 
    высота и основание, соотвественно.
    """

    def func(x, y): return x * y / 2

    # Вычисление половины произведения первого и второго элементов каждой строке матрицы
    result = [func(matrix[i][0], matrix[i][1]) for i in range(len(matrix))]

    return result


if __name__ == '__main__':

    # Ввод размера будущей матрицы
    size = int(input("Size of matrix = "))

    matrix = create_matrix(size)

    print("Matrix: ")
    print_matrix(matrix)

    print("\r\nAreas of triangles: ")
    print(triangles_area(matrix))

    print()
