import logging
from logging.handlers import (RotatingFileHandler)

from random import randint
import os

LOGGING_FILE_NAME = "log.log"

def logger_del_file():
    """
    Deleta arquivo de log. 
    Execute-o apenas uma vez em seu módulo __main__, antes de inicializar 
    o manipulador, neste caso a função logger_handler, abaixo.
    """
    try:
        if os.path.exists(LOGGING_FILE_NAME) and os.path.isfile(LOGGING_FILE_NAME):
            os.remove(LOGGING_FILE_NAME)
    except BaseException as e:
        print(f'\nErro ao deletar arquivo de log! {e}\n')

def logger_handler(name):
    """
    - Inicializa handler. 
    
    - name: nome do manipulador que você deseja registrar no arquivo de log 
    ao usar a variável paddrão %(name)s do parâmetro logging.Formatter.
    
    - Carregue-a em seu __main__, funções e módulos.
    
    - Exemplo: logger_xxx = logger_handler(__name__)
    """
    try:
        filelog = LOGGING_FILE_NAME
        formatlog = logging.Formatter('%(asctime)s; %(name)s; %(levelname)s; %(message)s')
        handler = RotatingFileHandler(filelog, mode='a',
                                        maxBytes=0, backupCount=0, 
                                        encoding='utf-8', delay=True, errors=None)
        handler.setFormatter(formatlog)
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)

        return logger
    except BaseException as e:
        print(f'\nErro ao inicializar log! {e}\n')

def logger_log(log, msg, level='info', printar=False):
    """
    - log = variável inicializada por logger_handler, acima.
    - level = debug; info; warning; error; critical and
    except for exc_info=True.
    """
    try:
        if printar == True:
            print(msg)    

        if level == 'debug':
            log.debug(f'{msg}')
        elif level == 'info':
            log.info(f'{msg}')
        elif level == 'warning':
            log.warning(f'{msg}')
        elif level == 'error':
            log.error(f'{msg}')
        elif level == 'critical':
            log.critical(f'{msg}')
        elif level == 'except':
            log.error(f'{msg}', exc_info=True)

    except BaseException as e:
        print(f'\nErro ao gravar log! {e}\n')

def teste_in():
    """
    testar comportamento do manipular quando usando a partir de uma função
    no mesmo módulo do inicializador do manipulador.
    """
    try:    
        logger_teste_in = logger_handler(__name__)

        lista = list(range(1000))
        for l in lista:
            div = randint(0, 5)
            x = l / div
            logger_log(logger_teste_in, f'{l} - x é igual a {x} no teste_in',)
    except BaseException as e:
        print(f'\nErro! {e}\n')
        logger_log(logger_teste_in, f'{e}', 'except', True)


