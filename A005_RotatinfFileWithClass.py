from random import randint

from modulos.A005_test_out import teste_out
from modulos.A005_handlerWithClass import Logger, teste_in

looger = Logger()
looger.del_file()
handler = looger.handler(__name__)

lista = list(range(10))

looger.log(handler, f'lista {lista}')

try:
    for l in lista:
        letra_size = chr(randint(ord('a'), ord('z')))
        looger.log(handler, f'item da lista {l} - {letra_size}')
except BaseException as e:
    print(f'\nErro! {e}\n')
    looger.log(handler, f'{e}', 'except', True)    

teste_in()
teste_out()
looger.log(handler, f'FIM', printar=True)