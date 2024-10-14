a = input("Aの値を入力:")
b = input("Bの値を入力:")

a = int(a)
b = int(b)

def GCD(a, b):
    while b:
        a, b = b, a % b
        return a

# 最大公約数を計算
gcd_result = GCD(a, b)
print(f"AとBの最大公約数は: {gcd_result}")

# 互いに素かどうかを判定
def is_coprime(a, b):
    return GCD(a, b) == 1

if is_coprime(a, b):
    print(f"{a}と{b}は互いに素です。")
else:
    print(f"{a}と{b}は互いに素ではありません。")