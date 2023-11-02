def area(a, h): 
    '''
    Функция, находящая площадь треугольника по заданной стороне и опущенной к ней высоте.
        
        Параметры:
            a (int, float) - первое число (сторона треугольника)
            h (int, float) - второе число (высота треугольника)
        
        Возвращаемое значение:
            area (int, float) - площадь треугольника с данной стороной и опущенной к ней высотой, высчитанная по математической формуле
            
    Пример вызова функции:
        area(3, 7) -> 10.5
    '''

    if type(a) != int and type(a) != float or type(h) != int and type(h) != float:
        return "Invalid parameters."

    if a < 0 or h < 0:
        return "Invalid parameters."

    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Функция, находящая периметр треугольника по заданным сторонам.
        
        Параметры:
            a (int, float) - первое число (первая сторона треугольника)
            b (int, float) - второе число (вторая сторона треугольника)
            c (int, float) - третье число (третья сторона треугольника)
        
        Возвращаемое значение:
            perimeter (int, float) - периметр треугольника с данными сторонами, высчитанный по математической формуле
            
    Пример вызова функции:
        perimeter(3, 7, 5) -> 15
    '''

    if type(a) != int and type(a) != float or type(b) != int and type(b) != float or type(c) != int and type(c) != float:
        return "Invalid parameters."

    if a < 0 or b < 0 or c < 0:
        return "Invalid parameters."

    return a + b + c 
