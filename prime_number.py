#TODO


# 自然数nをinputから取得
n = int(input("Enter a natural number: "))

def is_prime(n):
    # nが素数かどうかを判定し、bool値を返す
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 素数かどうかの結果を出力
print(f"{n} is prime: {is_prime(n)}")