#Dado 3 valores, retorne o maior

lista = []
while len(lista) < 3:
    a = int(input('Digite 3 números: '))
    lista.append(a)

for i in lista:
    maior = 0
    if i > maior:
        maior = i

print(maior)
