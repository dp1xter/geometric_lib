# Math formulas by Python Functions

## Python Math Module  
`math` — Mathematical functions and constants.  
Math module provides functions to deal with both basic operations such as addition(+), subtraction(-), multiplication(*), division(/) and advance operations like trigonometric, logarithmic, exponential functions.  
Math module provides various the value of various constants like pi, tau. Having such constants saves the time of writing the value of each constant every time we want to use it and that too with great precision. ***In this particular project from this module, the Pi constant is used to calculate the perimeter and area of a circle.***
```python
print(math.pi) -> 3.141592653589793
```

## Area

- ### Circle: S = πR²  
```python
def area(r):
    '''
    A function that finds the area of a circle with a given radius.
    
        Parameters:
            r (int, float) - number (the radius of the circle)
        
        Return Value:
            area (float) - area of the circle with the given radius, calculated by the mathematical formula
            
    Example of a return value:
        area(5.2) -> 84.94866535306801
    '''
    
    if type(r) != int and type(r) != float:
        return "Invalid parameters."

    if r < 0:
        return "Invalid parameters."
    
    return math.pi * r * r
```
**Input:** `print(area(5.2))` -> **Output:** `84.94866535306801`  

- ### Rectangle: S = ab  
```python  
def area(a, b):
    '''
    A function that finds the area of a rectangle with given sides.
        
        Parameters:
            a (int, float) - first number (the first side of the rectangle)
            b (int, float) - second number (the second side of the rectangle)
        
        Return Value:
            area (int, float) - area of a rectangle with given sides, calculated by a mathematical formula
            
    Example of a return value:
        area(2, 5) -> 10
    '''
    
    if type(a) != int and type(a) != float or type(b) != int and type(b) != float:
        return "Invalid parameters."

    if a < 0 or b < 0:
        return "Invalid parameters."
    
    return a * b 
```
**Input:** `print(area(2, 5))` -> **Output:** `10`  

- ### Square: S = a²  
```python  
def area(a):
    '''
    A function that finds the area of a square with a given side.
        
        Parameters:
            a (int, float) - number (the side of square)
        
        Return Value:
            area (int, float) - is the area of the square with the given side, calculated by the mathematical formula
            
    Example of a return value:
        area(2) -> 4
    '''
    
    if type(a) != int and type(a) != float:
        return "Invalid parameters."

    if a < 0:
        return "Invalid parameters."
    
    return a * a
```
**Input:** `print(area(2))` -> **Output:** `4`  

- ### Triangle: S = ah/2
```python
def area(a, h): 
    '''
    A function that finds the area of a triangle by a given side and the altitude lowered to it.
        
        Parameters:
            a (int, float) - first number (the side of a triangle)
            h (int, float) - second number (the height of the triangle)
        
        Return Value:
            area (int, float) - is the area of the triangle with the given side and the altitude lowered to it, calculated by the mathematical formula
            
    Example of a return value:
        area(3, 7) -> 10.5
    '''
    
    if type(a) != int and type(a) != float or type(h) != int and type(h) != float:
        return "Invalid parameters."

    if a < 0 or h < 0:
        return "Invalid parameters."
    
    return a * h / 2 
```
**Input:** `print(area(3, 7))` -> **Output:** `10.5`  

## Perimeter
- ### Circle: P = 2πR  
```python  
def perimeter(r):
    '''
    A function that finds the perimeter of a circle with a given radius.
    
        Parameters:
            r (int, float) - number (radius of the given circle)
        
        Return Value:
            perimeter (float) - the perimeter of the circle with the given radius, calculated using a mathematical formula
            
    Example of a return value:
        perimeter(3.5) -> 21.991148575128552
    '''
    
    if type(r) != int and type(r) != float:
        return "Invalid parameters."

    if r < 0:
        return "Invalid parameters."
    
    return 2 * math.pi * r
```
**Input:** `print(perimeter(3.5))` -> **Output:** `21.991148575128552`  

- ### Rectangle: P = 2a + 2b  
```python  
def perimeter(a, b): 
    '''
    A function that finds the perimeter of a rectangle with given sides.
        
        Parameters:
            a (int, float) - first number (the first side of the rectangle)
            b (int, float) - second number (the second side of the rectangle)
        
        Return Value:
            perimeter (int, float) - perimeter of a rectangle with given sides, calculated using a mathematical formula
            
    Example of a return value:
        perimeter(3.5, 2) -> 11.0
    '''
    
    if type(a) != int and type(a) != float or type(b) != int and type(b) != float:
        return "Invalid parameters."

    if a < 0 or b < 0:
        return "Invalid parameters."
    
    return 2 * (a + b)
```
**Input:** `print(perimeter(3.5, 2))` -> **Output:** `11.0`  

- ### Square: P = 4a  
```python  
def perimeter(a):
    '''
    A function that finds the perimeter of a square with a given side.
        
        Parameters:
            a (int, float) - number (the side of square)
        
        Return Value:
            perimeter (int, float) - perimeter of a square with a given side, calculated using a mathematical formula
            
    Example of a return value:
        perimeter(3) -> 12
    '''
    
    if type(a) != int and type(a) != float:
        return "Invalid parameters."

    if a < 0:
        return "Invalid parameters."
    
    return 4 * a
```
**Input:** `print(perimeter(3))` -> **Output:** `12`  

- ### Triangle: P = a + b + c  
```python
def perimeter(a, b, c): 
    '''
    A function that finds the perimeter of a triangle by given sides.
        
        Parameters:
            a (int, float) - first number (the first side of the triangle)
            b (int, float) - second number (the second side of the triangle)
            c (int, float) - third number (the third side of a triangle)
        
        Return Value:
            perimeter (int, float) - perimeter of a triangle with given sides, calculated using a mathematical formula
            
    Example of a return value:
        perimeter(3, 7, 5) -> 15
    '''
    
    if type(a) != int and type(a) != float or type(b) != int and type(b) != float or type(c) != int and type(c) != float:
        return "Invalid parameters."

    if a < 0 or b < 0 or c < 0:
        return "Invalid parameters."
    
    return a + b + c 
```
**Input:** `print(perimeter(3, 7, 5))` -> **Output:** `15`

## Unit-tests  

02.11.23 - Unit-tests added.  
The tests have been added to the [unit_tests](geometric_lib/unit_tests/) folder.

## Project change/Commits  

| Commit        | Changes                                      |
|---------------|----------------------------------------------|
| `2631a6a`     | Unit_tests added                             |
| `de69eff`     | Creating triangle.py + fixes in rectangle.py |
| `7f99951`     | Creating rectangle.py                        |
| `d078c8d`     | Docs added                                   |
| `8ba9aeb`     | Circle and square added                      |