#Para o maior:
lista = [1,2,3,4,5,6,7,8,9,-50,6346,1235436]
maior = lista[0]
for x in lista:
    if x > maior:
        maior = x

print(maior)

#Para o menor: Editar linha 4 para "if x < maior:"