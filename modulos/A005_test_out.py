# import random
from random import randint
from modulos.A005_handlerWithClass import Logger

def teste_out():
    """
    testar comportamento do manipular quando usando a partir de uma função
    em um módulo diferente do inicializador do manipulador.
    """
    try:
        looger = Logger()
        handler = looger.handler(__name__)

        lista = list(range(1000))
        for l in lista:
            div = randint(0, 5)
            k = l / div
            looger.log(handler, f"{l} - ok {k}")
    except BaseException as e:
        print(f'\nErro! {e}\n')
        looger.log(handler, f'Except {e}', 'except', True)