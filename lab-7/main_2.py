# Вариант программы для более 2 автобусных остановок
# Будет найдено общее число остановок для всех автобусов

def inp():
    while True:
        a = list(map(int, input().split()))
        if len(a) > 2 and len(a) % 2 == 0:
            return a
        else:
            print('Error. Number of bus stops should be multiple by 2.\r\n')


def routes(stops: list):
    if len(stops) == 2:
        return sorted(stops[0:2])
    return sorted(stops[0:2]) + routes(stops[2:])


def intersection(stops: list):
    a = intersection_helper(stops)
    return max(0, a[1] - a[0] + 1)


def intersection_helper(stops: list):
    if len(stops) == 4:
        return [max(stops[0], stops[2]), min(stops[1], stops[3])]
    return [max(stops[0], intersection_helper(stops[2:])[0]), min(stops[1], intersection_helper(stops[2:])[1])]


if __name__ == '__main__':
    print(intersection(routes(inp())))
