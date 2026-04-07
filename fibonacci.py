# "Escreva um programa que solicite ao usuário um número inteiro 
#e imprima os primeiros n
# números da sequência de Fibonacci." 

def fibo(numero): 
    lista = [0, 1]
    while (len(lista) - 1) <= numero:
        x = len(lista) - 1
        y = x - 1
        z = lista[x] + lista[y]
        lista.append(z)

        x += 1

    lista_dois = []
    for i in range(x - 1):
        lista_dois.append(lista[i])

    return lista_dois

e = int(input('Numero? '))
print(f'primeiros {e} numeros de Fibonacci: {fibo(e)}')
