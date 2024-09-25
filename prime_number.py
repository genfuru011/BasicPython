#TODO

def is_prime(n):
    prime = True
    if n < 2:
        prime = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break

    # 素数かどうかの結果を出力
    print(f"{n} is prime: {prime}")

# aとbを直接代入
a = 61
b = 10

# 結果を出力
is_prime(a)
is_prime(b)