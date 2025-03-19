#gerar uma senha segura - Min 12 caracteres, 3 Maisculos, 3 minustculos, 3 pontos.
#salvar senha em um arquivo

import string
import random
import time

mais = random.choices(string.ascii_uppercase, k = 4)
minus = random.choices(string.ascii_lowercase, k = 4)
digits = random.choices(string.digits, k = 4)
ponts = random.choices(string.punctuation, k = 4)

senha_lista = mais + minus + digits + ponts
random.shuffle(senha_lista)

senha = ''.join(senha_lista)

data_hora = time.strftime('%d/%m/%Y | %H:%M:%S | senha: ')

with open ('senha.txt', 'a') as arq:
    arq.write(f'{data_hora}')
    arq.write(f'{senha} \n')