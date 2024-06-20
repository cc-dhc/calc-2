import math
from cryptography.hazmat.backends import openssl
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from collections import Counter

# Função para gerar uma chave RSA
def generate_rsa_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend= openssl.backend
    )
    public_key = private_key.public_key()
    return public_key

# Gerar um conjunto de chaves
num_keys = 1000
keys = []
for i in range(num_keys):
#	print(f'{i}: gen key')
	keys.append(generate_rsa_key())

# Serializar as chaves públicas para comparar e contar frequências
serialized_keys = [key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
) for key in keys]

# Calcular a frequência de cada chave pública
key_frequencies = Counter(serialized_keys)

# Converter as frequências em uma função de densidade de probabilidade
def p(key):
    total_keys = len(serialized_keys)
    return key_frequencies[key] / total_keys if key in key_frequencies else 0

# Função de entropia
def entropy(key):
    px = p(key)
    return -px * math.log2(px) if px > 0 else 0

# Regra de Simpson 3/8 para integração numérica
def simpsons_3_8_rule(f, a, b, n):
    if n % 3 != 0:
        n += 3 - (n % 3)  # n deve ser múltiplo de 3 para a regra de Simpson 3/8

    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        xi = a + i * h
        if i % 3 == 0:
            integral += 2 * f(xi)
        else:
            integral += 3 * f(xi)

    return (3 * h / 8) * integral

# Como temos uma distribuição discreta de chaves, vamos usar os índices dos elementos como x
a = 0  # índice inicial
b = len(key_frequencies) - 1  # índice final
n = 10000  # número de subdivisões

# Para facilitar a integração, mapeamos os índices aos itens únicos na lista de chaves
unique_keys = list(key_frequencies.keys())

# Função de entropia ajustada para índices
def entropy_index(i):
    key_index = int(i)
    if key_index >= len(unique_keys):
        return 0
    key = unique_keys[key_index]
    return entropy(key)

# Calculando a integral da entropia
integral_value = simpsons_3_8_rule(entropy_index, a, b, n)
print(f"A entropia calculada das chaves RSA é: {integral_value} bits")

# Valor recomendado de entropia baseado na quantidade de chaves
recommended_entropy = math.log2(num_keys)
print(f"O valor recomendado de entropia para {num_keys} chaves é: {recommended_entropy:.2f} bits")

