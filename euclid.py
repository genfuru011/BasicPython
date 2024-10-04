a = input("Aの値を入力:")
b = input("Bの値を入力:")

#TODO

a = int(a)
b = int(b)

def GCD(a, b):
    while b:
        a, b = b, a % b
        return a
result = GCD(a,b)
print(f"AとBの最大公倍数は: {result}")