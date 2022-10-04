print('Programinha de contole de festa 2.0')
print('########################################')
numero_de_convidados = input('Coloque um numero de convidados: ')
lista_de_convidados = []

i = 1
while i <= int(numero_de_convidados) :
    nome_do_convidado = input('Coloque um nome do convidado #'+ str(i) +': ')
    lista_de_convidados.append(nome_do_convidado)
    i += 1

print('serao', numero_de_convidados, 'convidados')
print('LISTA DE CONVIDADOS')

for convidado in lista_de_convidados:
    print(convidado)