
import traceback 
from random import randint

from modulos.A006_funcoes import log_print, log_del
from modulos.A006_test_out import teste_out

log_del('file_log_name.log')

lista = range(6)
try:
    teste_out()
    for l in lista:
        letra_size = chr(randint(ord('a'), ord('z')))
        div = randint(1, 3)
        k = l / div
        msg = f"Escreva isso dentro do arquivo à Ãã Õõ áéíóú ÂÊÎÔÛ çÇ Üü: {l} - {letra_size}"
        log_print(msg, tela=False)
except BaseException as e:
    log_print(f'Erro!{traceback.format_exc()}', __name__, level='error', tela=False)
finally:
    print('fim')
