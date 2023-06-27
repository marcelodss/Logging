import logging
from logging.handlers import (RotatingFileHandler)

from random import randint
import os

class Teste:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

class Logger:
    def __init__(self):
        self.file_name = "log.log"

    def del_file(self):
        """
        Deleta arquivo de log. 
        Execute-o apenas uma vez em seu módulo __main__, antes de inicializar 
        o manipulador, neste caso a função logger_handler, abaixo.
        - Exemplo:
        Instancie a classe <-looger=Logger()-> e chame método <-looger.del_file()->
        """
        try:
            if os.path.exists(self.file_name) and os.path.isfile(self.file_name):
                os.remove(self.file_name)
        except BaseException as e:
            print(f'\nErro ao deletar arquivo de log! {e}\n')

    def handler(self, name):
        """
        - Inicializa handler. 
        
        - name: nome do manipulador que você deseja registrar no arquivo de log 
        ao usar a variável paddrão %(name)s do parâmetro logging.Formatter.
        
        - Carregue-a em seu __main__, funções e módulos.
        
        - Exemplo:
        Instancie a classe <-looger=Logger()-> e crie uma variável com os dados do manipulador <-handler=looger.handler(__name__)->
        """
        try:
            filelog = self.file_name
            
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

    def log(self, log, msg, level='info', printar=False):
        """
        - log = variável inicializada por handler, acima.
        - level = debug; info; warning; error; critical e except com exc_info=True.
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
        looger = Logger()
        handler = looger.handler(__name__)

        lista = list(range(1000))
        for l in lista:
            div = randint(0, 5)
            x = l / div
            looger.log(handler, f'{l} - x é igual a {x} no teste_in',)
    except BaseException as e:
        print(f'\nErro! {e}\n')
        looger.log(handler, f'{e}', 'except', True)
