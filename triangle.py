def area(a, h): 
    '''
    Функция, находящая площадь треугольника по заданной стороне и опущенной к ней высоте.
        
        Параметры:
            a (int, float, etc...) - первое число (сторона треугольника)
            h (int, float, etc...) - второе число (высота треугольника)
        
        Возвращаемое значение:
            area (int, float, etc...) - площадь треугольника с данной стороной и опущенной к ней высотой, высчитанная по математической формуле
            
    Пример вызова функции:
        area(3, 7) -> 10.5
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Функция, находящая периметр треугольника по заданным сторонам.
        
        Параметры:
            a (int, float, etc...) - первое число (первая сторона треугольника)
            b (int, float, etc...) - второе число (вторая сторона треугольника)
            c (int, float, etc...) - третье число (третья сторона треугольника)
        
        Возвращаемое значение:
            perimeter (int, float, etc...) - периметр треугольника с данными сторонами, высчитанный по математической формуле
            
    Пример вызова функции:
        perimeter(3, 7, 5) -> 15
    '''
    return a + b + c 
