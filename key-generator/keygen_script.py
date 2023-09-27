import random
from Crypto.Util.number import getPrime, GCD, inverse


def generate_rsa_keys():
    # Генерація простих чисел p та q
    p = getPrime(16)
    q = getPrime(16)

    # Обчислення n та функції Ейлера (phi)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Вибір відкритого експонента e
    e = random.randint(2, phi - 1)
    while GCD(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Обчислення закритого експонента d
    d = inverse(e, phi)

    # Повертаємо пари ключів: відкритий ключ (e, n) та закритий ключ (d, n)
    return [str(e), str(n)], [str(d), str(n)]
