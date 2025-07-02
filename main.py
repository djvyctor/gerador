import random
from faker import Faker

fake = Faker('pt_BR')

def gerar_telefones_goias(quantidade):
    telefones = []
    for _ in range(quantidade):
        telefone = f"(62) 9{random.randint(1000, 9999):04d}-{random.randint(1000, 9999):04d}"
        telefones.append(telefone)
    return telefones

qtd = int(input("Quantos telefones com DDD 62 deseja gerar? "))
lista_telefones = gerar_telefones_goias(qtd)

print("\nTelefones gerados (DDD 62):")
for telefone in lista_telefones:
    print(telefone)
print("-" * 30)