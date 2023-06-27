
from random import randint
 
from modulos.A004_handlerWithFunction import logger_handler, logger_log, logger_del_file, teste_in
from modulos.A004_test_out import teste_out

logger_del_file()
logger_main = logger_handler(__name__)

lista = list(range(10))

logger_log(logger_main, f'lista {lista}')

try:
    for l in lista:
        letra_size = chr(randint(ord('a'), ord('z')))
        logger_log(logger_main, f'item da lista {l} - {letra_size}')
except BaseException as e:
    print(f'\nErro! {e}\n')
    logger_log(logger_main, f'{e}', 'error', True)    

teste_in()
teste_out()
logger_log(logger_main, f'FIM', printar=True)

