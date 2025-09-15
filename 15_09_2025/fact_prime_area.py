def factorial(n):
    if n == 0:
        raise ValueError(" cannot divid by zero")
    
    if n < 0:
        return "Factorial not defined for negative numbers."
    result = 1
    
    for i in range(2, n + 1):
        result *= i
    return result

def prime(n):
    if n == 0:
        raise ValueError("value can not be 0!!!")
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def circlearea(radias):
    if radias == 0:
        raise ValueError("zero radius")
    area = 3.14*radias**2
    print(f"Area of the circle:", area)
    return area
