# import random
from random import randint

from modulos.A004_handlerWithFunction import logger_handler, logger_log

def teste_out():
    """
    testar comportamento do manipular quando usando a partir de uma função
    em um módulo diferente do inicializador do manipulador.
    """
    try:
        logger_teste_out = logger_handler(__name__)

        lista = list(range(1000))
        for l in lista:
            div = randint(0, 5)
            k = l / div
            logger_log(logger_teste_out, f"{l} - ok {k}")
    except BaseException as e:
        print(f'\nErro! {e}\n')
        logger_log(logger_teste_out, f'Except {e}', 'except', True)