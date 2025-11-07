# 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

son = int(input("Son kiriting: "))
print("Faktorial:", factorial(son))

# 2
def palindrom(s):
    return s == s[::-1]

matn = input("So'z yoki matn kiriting: ")
print("Palindrommi:", palindrom(matn))

# 3
def katta_kichik(royxat):
    return max(royxat), min(royxat)

sonlar = list(map(int, input("Sonlarni kiriting (bo'sh joy bilan ajrating): ").split()))
katta, kichik = katta_kichik(sonlar)
print("Eng katta:", katta)
print("Eng kichik:", kichik)

# 4
def unli_soni(matn):
    unlilar = "aeiouAEIOUаеиоуўяюёэАЕИОУЎЯЮЁЭ"
    return sum(1 for harf in matn if harf in unlilar)

matn = input("Matn kiriting: ")
print("Unli harflar soni:", unli_soni(matn))

# 5
def tubmi(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

son = int(input("Son kiriting: "))
print("Tub sonmi:", tubmi(son))

# 6
def teskari_royxat(royxat):
    return royxat[::-1]

royxat = input("Ro'yxat elementlarini kiriting: ").split()
print("Teskari ro'yxat:", teskari_royxat(royxat))

# 7
def kalkulyator(a, b, amal):
    if amal == '+': return a + b
    elif amal == '-': return a - b
    elif amal == '*': return a * b
    elif amal == '/': return a / b if b != 0 else "Bo‘lish mumkin emas!"
    else: return "Noto‘g‘ri amal!"

a = float(input("Birinchi son: "))
b = float(input("Ikkinchi son: "))
amal = input("Amalni kiriting (+, -, *, /): ")
print("Natija:", kalkulyator(a, b, amal))

# 8
def sozlar_soni(matn):
    return len(matn.split())

matn = input("Matn kiriting: ")
print("So'zlar soni:", sozlar_soni(matn))

# 9
def juft_ikkilantirish(royxat):
    return [x * 2 if x % 2 == 0 else x for x in royxat]

royxat = list(map(int, input("Sonlarni kiriting: ").split()))
print("Natija:", juft_ikkilantirish(royxat))

# 10
def kalitlar_royxati(lugat):
    return list(lugat.keys())

lugat = {}
n = int(input("Nechta element kiritmoqchisiz? "))
for i in range(n):
    k = input(f"{i+1}-kalitni kiriting: ")
    v = input(f"{i+1}-qiymatni kiriting: ")
    lugat[k] = v

print("Kalitlar ro'yxati:", kalitlar_royxati(lugat))




