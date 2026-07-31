"""
Secret Number é um jogo onde você deve descobrir um valor secreto no menor número de tenativas

1# gera um número aleatório
2# usuário faz a tentativa
    2.1#erra, retorna no 2#
3#acerta = acaba e impreme o número de tentativas
"""

from random import random
import os

all_secret=[]

def ask():
    ask_user= input('Coloque um valor: ')

    try:
        ask_user=int(ask_user)
        return ask_user
    
    except ValueError:
        print('Você não colocou um número')

'''
Definição do numéro aleatório
'''
def random_number_function():
    range_sys=10 #apenas multiplus de 10
    random_number=int(random()*range_sys+1) #função random() gera um número aleatório decimal 0.1 - rangesys muda isso para 1.0 - int muda para 1 - +1 muda o range de (0-9) -> (0-10)
    return random_number

'''
Sistema de tentativas
'''

def try_try():
    '''
    Não repetir o número secreto
    '''
    secret_number = random_number_function()

    while secret_number in all_secret: #enquanto secret number existir em all secret ele vai re sortear até ele não existir na lista
        secret_number = random_number_function()

    #all_secret.append(secret_number)
    #print(all_secret)
    os.system('cls')
    user_try=1


    while True:
        #print(secret_number) #apague
        user_in=ask()

        if user_in==secret_number:
            print(f'\nParabéns você acertou!!! com um número de tentativas de {user_try} | SECRET NUMBER = {secret_number}')
            break
        else:
            os.system('cls')
            print('\nErrouuuuuuuuuuuuuuuuuu Tente novamente\n')
            user_try+=1

            if secret_number>user_in:
                print(f'O número secreto é maior que {user_in} - tentativas: {user_try}')
            else:
                print(f'O número secreto é menor que {user_in} - tentativas: {user_try}')


def main():

    try_try()

    while True:

        #loop
        len_list=len(all_secret)
        #print(len_list)#apague

        if len_list >= 10:
            print('Você atingiu o número máximo de sorteios, bye')
            break
        else:
            again=input('Deseja jogar novamente? (y/n): ')
            again=again.upper()

            if again == 'Y':
                try_try()

            else:
                print('bye')
                break
               
if __name__=='__main__':
    main()