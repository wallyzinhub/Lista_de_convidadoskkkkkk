numero = 0

while True:
    print(numero)
    if numero == 5:
        break
    numero += 1

pessoa1 = input('Seu nome convidado1: ')
pessoa2 = input('seu nome convidado2: ')
pessoa3 = input('Seu nome convidado3: ')
pessoa4 = input('Seu nome convidado4: ')
pessoa5 = input('Seu nome convidado5: ')

lista_de_pessoas = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5]

print('Os convidados sao:', lista_de_pessoas)