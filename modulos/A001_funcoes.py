import logging

def logging_basicConfig():
    LEVEL = logging.DEBUG
    FILE_NAME = "programa.log"
    FORMAT = "%(asctime)s - %(levelname)s - %(message)s - %(filename)s (linha: %(lineno)d)"
    ENCODING = 'utf-8'
    logging.basicConfig(
        level=LEVEL, 
        filename=FILE_NAME, 
        encoding=ENCODING,
        format=FORMAT,
    )

def resultado_operacional(faturamento, custo):
    return faturamento - custo

def lucro_liquido(faturamento, custo, percentual_imposto):
    if percentual_imposto == 0:
        logging.warning("Percentual de imposto é 0, tá certo isso?")
    return (faturamento - custo) * (1 - percentual_imposto)

def lucro_por_acoes(faturamento, custo, percentual_imposto, acoes):
    try:
        if acoes == 0:
            logging.warning("Ações não pode ser igual a 0")
        return lucro_liquido(faturamento, custo, percentual_imposto) / acoes
    except Exception as e:
        print(f"Erro: {e}")
        logging.exception("Exception occurred")