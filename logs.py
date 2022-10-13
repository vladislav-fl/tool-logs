from staff.logic import *

# ONLY 1 LOG PER FUNCTION CALL!!!
# PREFIX_TYPE = LOG_ID, NONE, CUSTOM

# Нужно переместить константы в поле экземпляров класса из внешнего чтобы каждый экземпляр работал со своими константами
# То есть, общие константы (версия, стабильность) будут у всех объектов одинаковые, а тип вывода и путь свои для каждого

# Переместить данные из const.py в json

# Установить проверку добавления данных в JSON (чтобы были пары ключ - значение)
# Добавить в json добавление не просто текста, а данных в существующий словарь, либо его создание

# Сделать тесты и исправить ошибки

# Добавить лог в линию и id лога в http

class Log():
    """
        Main class for working with Logs.
    """
    def __init__(self, return_status: bool = True, prefix_type: str = 'LOG_ID', prefix: str = '') -> None:
        """
            Set argumets in the way you want to use Log functions

            `return_status` - set `True` if you need Status class to be returned to variable while working with Logs
            
            `prefix_type` - set `LOG_ID`, `CUSTOM` if you need to add log id or your own message to logs, or set `NONE` if you dont want to add any message to logs
            
            `prefix` - set '' if you dont want any message added to your logs (dont forget to set `prefix_type` to 'NONE'), or give your custom message (and set `prefix_type` to `LOG_ID` or `CUSTOM`)

            Example:
            `log` = Log(`return_status` = True, `prefix_type` = 'NONE', `prefix` = '')
        """
        Settings.PREFIX_TYPE = prefix_type
        Settings.PREFIX = prefix
        Settings.RETURN_STATUS = return_status

    def json(self, path: str, log: Union[dict, list]) -> Optional[Settings.Status]:
        """
        
        """
        Settings.STREAM_LOG = log
        Settings.STREAM_PATH = path
        
        try:
            with open(Settings.STREAM_PATH, 'a') as file:
                with open(Settings.STREAM_PATH, 'r') as file_reader:
                    if file_reader.read() != '':
                        file.write(',')
                    file_reader.close()
                dump(Settings.STREAM_LOG, file)
                file.close()
        except:
            Settings.Status.ID = Errors.CANT_OPEN_JSON_FILE['ID']
            Settings.Status.MESSAGE = Errors.CANT_OPEN_JSON_FILE['MESSAGE']

            return Settings.Status if Settings.RETURN_STATUS else None
        
        Settings.LOG_ID += 1
        Settings.Status.ID = Messages.OPERATION_DONE['ID']
        Settings.Status.MESSAGE = Messages.OPERATION_DONE['MESSAGE']

        return Settings.Status if Settings.RETURN_STATUS else None

    def txt(self, path: str, log: any) -> Optional[Settings.Status]:
        Settings.STREAM_LOG = str(log)
        Settings.STREAM_PATH = path

        if Settings.PREFIX_TYPE == 'LOG_ID':
            Settings.STREAM_LOG = f'[{str(Settings.LOG_ID)}] ' + Settings.STREAM_LOG
        elif Settings.PREFIX_TYPE == 'CUSTOM':
            Settings.STREAM_LOG = f'{str(Settings.PREFIX)} ' + Settings.STREAM_LOG
        elif Settings.PREFIX_TYPE == 'NONE':
            pass
        else:
            Settings.Status.ID = Warnings.WRONG_PREFIX_TYPE_WHILE_STREAMING['ID']
            Settings.Status.MESSAGE = Warnings.WRONG_PREFIX_TYPE_WHILE_STREAMING['MESSAGE']

            return Settings.Status if Settings.RETURN_STATUS else None

        try:
            with open(Settings.STREAM_PATH, 'a') as file:
                file.write(Settings.STREAM_LOG + '\n')
                file.close()
        except:
            Settings.Status.ID = Errors.CANT_OPEN_TXT_FILE['ID']
            Settings.Status.MESSAGE = Errors.CANT_OPEN_TXT_FILE['MESSAGE']

            return Settings.Status if Settings.RETURN_STATUS else None
        
        Settings.LOG_ID += 1
        Settings.Status.ID = Messages.OPERATION_DONE['ID']
        Settings.Status.MESSAGE = Messages.OPERATION_DONE['MESSAGE']

        return Settings.Status if Settings.RETURN_STATUS else None

    def http(self, path: str, log: any) -> Optional[Settings.Status]:
        Settings.STREAM_LOG = str(log)
        Settings.STREAM_PATH = path

        if Settings.PREFIX_TYPE == 'LOG_ID':
            Settings.STREAM_LOG = f'[{str(Settings.LOG_ID)}] ' + Settings.STREAM_LOG
        elif Settings.PREFIX_TYPE == 'CUSTOM':
            Settings.STREAM_LOG = f'{str(Settings.PREFIX)} ' + Settings.STREAM_LOG
        elif Settings.PREFIX_TYPE == 'NONE':
            pass
        else:
            Settings.Status.ID = Warnings.WRONG_PREFIX_TYPE_WHILE_STREAMING['ID']
            Settings.Status.MESSAGE = Warnings.WRONG_PREFIX_TYPE_WHILE_STREAMING['MESSAGE']

            return Settings.Status if Settings.RETURN_STATUS else None

        response: Response = post(url=Settings.STREAM_PATH, data=Settings.STREAM_LOG)

        if response.status_code == 200:
            Settings.Status.ID = Messages.OPERATION_DONE['ID']
            Settings.Status.MESSAGE = Messages.OPERATION_DONE['MESSAGE']

            return Settings.Status if Settings.RETURN_STATUS else None

        else:
            Settings.Status.ID = Errors.HTTP_RETURNED_BAD_STATUS['ID']
            Settings.Status.MESSAGE = Errors.HTTP_RETURNED_BAD_STATUS['MESSAGE'] + ': ' + str(response.status_code)

            return Settings.Status if Settings.RETURN_STATUS else None

    def print(self, log: any) -> Optional[Settings.Status]:
        Settings.STREAM_LOG = str(log)
        Settings.STREAM_PATH = ''

        if Settings.PREFIX_TYPE == 'LOG_ID':
            Settings.STREAM_LOG = f'[{str(Settings.LOG_ID)}] ' + Settings.STREAM_LOG
        elif Settings.PREFIX_TYPE == 'CUSTOM':
            Settings.STREAM_LOG = f'{str(Settings.PREFIX)} ' + Settings.STREAM_LOG
        elif Settings.PREFIX_TYPE == 'NONE':
            pass
        else:
            Settings.Status.ID = Warnings.WRONG_PREFIX_TYPE_WHILE_STREAMING['ID']
            Settings.Status.MESSAGE = Warnings.WRONG_PREFIX_TYPE_WHILE_STREAMING['MESSAGE']

            return Settings.Status if Settings.RETURN_STATUS else None

        print(Settings.STREAM_LOG)

        Settings.Status.ID = Messages.OPERATION_DONE['ID']
        Settings.Status.MESSAGE = Messages.OPERATION_DONE['MESSAGE']

        return Settings.Status if Settings.RETURN_STATUS else None

    def program() -> Optional[Settings.Status]:
        pass

    # Добавить все константы в настройках в какой-либо словарь, чтобы по переменной content доставать их и показывать
    def check_settings(self, content: str = '*'):
        pass

    def change_settings():
        pass

    def set_id_to_one(self, ):
        Settings.LOG_ID = 1

        Settings.Status.ID = Messages.OPERATION_DONE['ID']
        Settings.Status.MESSAGE = Messages.OPERATION_DONE['MESSAGE']

        return Settings.Status if Settings.RETURN_STATUS else None
