# import random
from random import randint
import traceback 
from modulos.A006_funcoes import log_print

def teste_out():
    """
    testar comportamento do manipular quando usando a partir de uma função
    em um módulo diferente do inicializador do manipulador.
    """
    try:
        lista = list(range(10))
        for l in lista:
            div = randint(1, 5)
            k = l / div
            log_print(f"{l} - ok {k}", __name__, tela=True)
    except BaseException as e:
        log_print(f'Erro!{traceback.format_exc()}', __name__, level='error', tela=True)