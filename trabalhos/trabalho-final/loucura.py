from collections import Counter
import random
import math
from Crypto.Util import number

# Função para gerar chaves RSA
def generate_rsa_key(bits=2048):
    p = number.getPrime(bits // 2)
    q = number.getPrime(bits // 2)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 65537  # Valor comum para e
    d = number.inverse(e, phi_n)

    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

# Função de entropia direta
def calculate_entropy(frequencies, num_samples):
    entropy = 0.0
    for count in frequencies.values():
        p = count / num_samples
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

# Gerar um conjunto de chaves
num_keys = 1000
print(f"Gerando {num_keys} chaves RSA de 2048 bits...")
keys = []  # Usando apenas a chave pública
for i in range(num_keys):
    print(i)
    keys.append(generate_rsa_key(2048)[0])


# Serializar as chaves públicas para comparar e contar frequências
serialized_keys = [str(key) for key in keys]

# Calcular a frequência de cada chave pública
key_frequencies = Counter(serialized_keys)
print(f"Calculadas as frequências das chaves geradas.")

# Calculando a entropia diretamente a partir das frequências
print(f"Calculando a entropia diretamente das frequências das chaves geradas...")
entropy_value = calculate_entropy(key_frequencies, num_keys)
print(f"A entropia calculada das chaves RSA é: {entropy_value} bits")

# Valor recomendado de entropia baseado na quantidade de chaves
recommended_entropy = math.log2(num_keys)
print(f"O valor recomendado de entropia para {num_keys} chaves é: {recommended_entropy:.2f} bits")

print("Execução concluída.")
