import cmath

coefficients = [
    (1, -6, 9),   
    (1, 2, -8),    
    (8, -6, -35),  
    (1, 0, 1)
]

for a,b,c in coefficients:
    # 判別式を計算
    D = cmath.sqrt(b**2 - 4*a*c)
    
    # 2つの解を計算
    x1 = (-b + D) / (2 * a)
    x2 = (-b - D) / (2 * a)

    print(x1, x2)



