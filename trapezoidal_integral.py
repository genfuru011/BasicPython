import math

def trapezoidal_integration(f, a=0, b=1, n=100):
   
    
    h = (b - a) / n  
    x = a
    s = 0.5 * f(a)
    for i in range(1, n):
        x += h
        s += f(x)
    s += 0.5 * f(b)
    return s * h

def f1(x):
    return math.sin(x)
result1 = trapezoidal_integration (f1, 0, math.pi / 2, 50)
print("問題 (1) の積分値:", result1)
    
def f2(x):
    return 4 / (1 + x**2)
result2 = trapezoidal_integration (f2, 0, 1, 100)
print("問題（２）の積分値:", result2)

def f3(x):
    return math.sqrt(math.pi) * math.exp(-x**2)
result3 = trapezoidal_integration(f3, -100, 100, 1000)
print("問題 (3) の積分値:", result3)