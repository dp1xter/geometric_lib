
def area(a):
    '''
    Функция, находящая площадь квадрата с заданной стороной.

        Параметры:
            a (int, float) - число (сторона квадрата)

        Возвращаемое значение:
            area (int, float) - площадь квадрата с данной стороной, высчитанная по математической формуле

    Пример вызова функции:
        area(2) -> 4
    '''

    if type(a) != int and type(a) != float:
        return "Invalid parameters."

    if a < 0:
        return "Invalid parameters."

    return a * a


def perimeter(a):
    '''
    Функция, находящая периметр квадрата с заданной стороной.

        Параметры:
            a (int, float) - число (сторона квадрата)

        Возвращаемое значение:
            perimeter (int, float) - периметр квадрата с данной стороной, высчитанный по математической формуле

    Пример вызова функции:
        area(3) -> 12
    '''

    if type(a) != int and type(a) != float:
        return "Invalid parameters."

    if a < 0:
        return "Invalid parameters."

    return 4 * a
