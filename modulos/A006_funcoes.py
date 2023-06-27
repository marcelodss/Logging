import datetime, os
import json 

LOGGING_FILE_NAME = "log.log"
PATH_LOG = "log"

def log_settings_file(action="", file_name=LOGGING_FILE_NAME):
    try:
        if file_name == '':
            file_name = LOGGING_FILE_NAME
        # ====================================================
        json_file_name = "settings.json"
        settings = {'file_log_name': file_name}
        # ====================================================
        if action == 'set': # set arquivo json com nome do arquivo de log a ser utilizado
            if os.path.exists(PATH_LOG) and os.path.isfile(PATH_LOG):
                os.remove(PATH_LOG)
            if os.path.exists(PATH_LOG) == False:
                os.mkdir(PATH_LOG)
            with open(f"{PATH_LOG}\\{json_file_name}", "w", encoding='utf-8') as outfile: 
                json.dump(settings, outfile, indent=4) 
        else: # retorna nome do arquivo de log a ser utilizado
            if os.path.exists(f"{PATH_LOG}\\{json_file_name}") and os.path.isfile(f"{PATH_LOG}\\{json_file_name}"):
                with open(f"{PATH_LOG}\\{json_file_name}", 'r', encoding='utf-8') as openfile: 
                    settings_loaded = json.load(openfile) 
                return f"{PATH_LOG}\\{settings_loaded['file_log_name']}"
            else:
                return f"{PATH_LOG}\\{LOGGING_FILE_NAME}"
    except BaseException as e:
        print(f'\nErro ao criar arquivo de configurações para log! {e}\n')

def log_del(file_name=LOGGING_FILE_NAME):
    """
    Deleta arquivo de log. 
    Execute-o apenas uma vez em seu módulo __main__, antes de utilizar
    a função log_print, abaixo.
    """
    try:
        # Cria arquivo json contendo nome do arquivo de log a ser utilizado
        log_settings_file('set', file_name)
        # Deelta arquivo de log
        if os.path.exists(f'{PATH_LOG}\\{file_name}') and os.path.isfile(f'{PATH_LOG}\\{file_name}'):
            os.remove(f'{PATH_LOG}\\{file_name}')
    except BaseException as e:
        print(f'\nErro ao deletar arquivo de log! {e}\n')

def log_print(msg, source="", level='info', tela=False):
    try:
        """
        level = debug; info; warning; error; critical
        """
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_log = log_settings_file()

        if tela == True:
             print(msg)

        with open(file_log, 'a', encoding='utf-8') as f:
            print(f'{now} {level.upper()} {msg} {source}', file=f)

    except BaseException as e:
        print(f'\nErro ao regitrar log: {e}')
