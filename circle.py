import math
import unittest

def area(r):
    '''
    Функция, находящая площадь круга с заданным радиусом.
    
        Параметры:
            r (int, float) - число (радиус данного круга)
        
        Возвращаемое значение:
            area (float) - площадь круга с данным радиусом, высчитанная по математической формуле
            
    Пример вызова функции:
        area(5.2) -> 84.94866535306801
    '''

    if type(r) != int and type(r) != float:
        return "Invalid parameters."

    if r < 0:
        return "Invalid parameters."

    return math.pi * r * r


def perimeter(r):
    '''
    Функция, находящая периметр круга/окружности с заданным радиусом.
    
        Параметры:
            r (int, float) - число (радиус данного круга/окружности)
        
        Возвращаемое значение:
            perimeter (float) - периметр круга/окружности с данным радиусом, высчитанный по математической формуле
            
    Пример вызова функции:
        perimeter(3.5) -> 21.991148575128552
    '''

    if type(r) != int and type(r) != float:
        return "Invalid parameters."

    if r < 0:
        return "Invalid parameters."

    return 2 * math.pi * r
