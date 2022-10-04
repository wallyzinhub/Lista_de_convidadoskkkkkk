idade = input('Informe sua idade:')
peso = input('Informe seu peso:')
altura = input('Informe sua altura:')

if int(idade) < 18 or int(peso) < 50 or float(altura) < 1.70:
    print('Infelizmente voce nao esta apto para entrar no exercito')
else:
    print('PARABENS!!! voce esta totalmente apto\npara entrar ao exercito')