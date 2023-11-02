def area(a, b):
    '''
    Функция, находящая площадь прямоугольника с заданными сторонами.
        
        Параметры:
            a (int, float) - первое число (первая сторона прямоугольника)
            b (int, float) - второе число (вторая сторона прямоугольника)
        
        Возвращаемое значение:
            area (int, float) - площадь прямоугольника с данными сторонами, высчитанная по математической формуле
            
    Пример вызова функции:
        area(2, 5) -> 10
    '''

    if type(a) != int and type(a) != float or type(b) != int and type(b) != float:
        return "Invalid parameters."

    if a < 0 or b < 0:
        return "Invalid parameters."

    return a * b 

def perimeter(a, b): 
    '''
    Функция, находящая периметр прямоугольника с заданными сторонами.
        
        Параметры:
            a (int, float) - первое число (первая сторона прямоугольника)
            b (int, float) - второе число (вторая сторона прямоугольника)
        
        Возвращаемое значение:
            perimeter (int, float) - периметр прямоугольника с данными сторонами, высчитанный по математической формуле
            
    Пример вызова функции:
        perimeter(3.5, 2) -> 11.0
    '''

    if type(a) != int and type(a) != float or type(b) != int and type(b) != float:
        return "Invalid parameters."

    if a < 0 or b < 0:
        return "Invalid parameters."

    return 2 * (a + b)
