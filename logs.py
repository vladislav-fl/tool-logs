import staff.logic as logic
import staff.const as const

import logging
import json

import requests

# Сделать возврат какого-либо ответа от каждой функции после вызова ver, set, rtn и тд - Check
# Добавить вариант нескольких потоков выхода - Check
# Добавить тестовую проверку на правильное соединение - Check

# Нужно переместить константы в поле экземпляров класса из внешнего чтобы каждый экземпляр работал со своими константами
# То есть, общие константы (версия, стабильность) будут у всех объектов одинаковые, а тип вывода и путь свои для каждого

# Переместить данные из const.py в json

# В аргументах set функции у аргумента return_path указать не любые принимаемые данные, а конкретно bool или str (ну или еще что то, если додумаюсь :))

# Перенести всю логику программы (ключевые функции, а возможно и сам класс в logic.py)

# Установить проверку добавления данных в JSON (чтобы были пары ключ - значение)
# Добавить в json добавление не просто текста, а данных в существующий словарь, либо его создание

# Добавить коды ошибок

# Сделать тесты и исправить ошибки

# Добавить лог в линию и id лога в http

class Log:
    """

        Main class for working with Logs.

    """
    
    def __txt(self, ):
        with open(const.Settings.RETURN_PATH, 'a') as txt_file:
            if not const.Settings.NEED_TO_RETURN_LOG_ID and not const.Settings.OBJECTS_IN_ONE_LINE:
                for object in const.Settings.RETURN_MESSAGE:
                    txt_file.write(object + '\n')

            elif const.Settings.NEED_TO_RETURN_LOG_ID and not const.Settings.OBJECTS_IN_ONE_LINE:
                for object in const.Settings.RETURN_MESSAGE:
                    txt_file.write(f'[{const.Settings.LOG_ID}] - ' + object + '\n')

            elif const.Settings.NEED_TO_RETURN_LOG_ID and const.Settings.OBJECTS_IN_ONE_LINE:
                line_log: str = ''
                for object in const.Settings.RETURN_MESSAGE:
                    line_log += object
                txt_file.write(f'[{const.Settings.LOG_ID}] - ' + line_log + '\n')
                del line_log

            elif not const.Settings.NEED_TO_RETURN_LOG_ID and const.Settings.OBJECTS_IN_ONE_LINE:
                line_log: str = ''
                for object in const.Settings.RETURN_MESSAGE:
                    line_log += object
                print(line_log)
                txt_file.write(line_log + '\n')
                del line_log

            txt_file.close()
            
        return const.Messages.OPERATION_DONE['ID'], const.Messages.OPERATION_DONE['MESSAGE']

    def __json(self, ):
        with open(const.Settings.RETURN_PATH, 'a') as json_file:
            if not const.Settings.NEED_TO_RETURN_LOG_ID and not const.Settings.OBJECTS_IN_ONE_LINE:
                for object in const.Settings.RETURN_MESSAGE:
                    json.dump(object + '\n', json_file)

            elif const.Settings.NEED_TO_RETURN_LOG_ID and not const.Settings.OBJECTS_IN_ONE_LINE:
                for object in const.Settings.RETURN_MESSAGE:
                    json.dump(f'[{const.Settings.LOG_ID}] - ' + object + '\n', json_file)

            elif const.Settings.NEED_TO_RETURN_LOG_ID and const.Settings.OBJECTS_IN_ONE_LINE:
                line_log: str = ''
                for object in const.Settings.RETURN_MESSAGE:
                    line_log += object
                json.dump(f'[{const.Settings.LOG_ID}] - ' + line_log + '\n', json_file)
                del line_log

            elif not const.Settings.NEED_TO_RETURN_LOG_ID and const.Settings.OBJECTS_IN_ONE_LINE:
                line_log: str = ''
                for object in const.Settings.RETURN_MESSAGE:
                    line_log += object
                json.dump(line_log + '\n', json_file)
                del line_log
            
            json_file.close()

        return const.Messages.OPERATION_DONE['ID'], const.Messages.OPERATION_DONE['MESSAGE']

    # http session always use POST method to connect with server and return it stream
    def __http(self, ):
        for object in const.Settings.RETURN_MESSAGE:
            response: requests.Response = requests.post(url=const.Settings.RETURN_PATH, data=object)
            if response.status_code == 200:
                # Return info that all OK
                return const.Messages.OPERATION_DONE['ID'], const.Messages.OPERATION_DONE['MESSAGE']
            else:
                return const.Errors.HTTP_RETURNED_BAD_STATUS['ID'], const.Errors.HTTP_RETURNED_BAD_STATUS['MESSAGE'] + ': ' + str(response.status_code)
                # Return info that error accured during this command and send response status code
    
    def set(self, return_type: str = 'DEV_CONSOLE', return_path: any = None, return_status_by_default: bool = True, test: bool = False, need_to_return_log_id: bool = False, objects_in_one_line: bool = False) -> const.Settings.Status:
        """
        
            Makes start changes where You should set type of output stream, output path etc.
            
            Call this function at the beginning and each time you want to change settings.

            Commonly `rtn` function will return objects to the common stream (in which would return `print` function) if return type is not given.
        
            Commonly `return_path` is None because `return_type` is `DEV_CONSOLE` if nothing is given. 
            You should give path to the file if you are going to use `TXT`, `JSON` etc. as output stream.

            Set test = True to test connection and get status of operation. It is recommended to test connection before using its stream.

            Test will send to work stream empty message just to test connection.

            If You want, there is opportunity not to use set function and leave all constants as they are.

        """
        const.Settings.RETURN_TYPE = return_type
        const.Settings.RETURN_PATH = return_path
        const.Settings.RETURN_STATUS_BY_DEFAULT = return_status_by_default
        const.Settings.TEST = test
        const.Settings.NEED_TO_RETURN_LOG_ID = need_to_return_log_id
        const.Settings.OBJECTS_IN_ONE_LINE = objects_in_one_line
        
        if const.Settings.TEST:
            return self.rtn('')
        elif not const.Settings.TEST:
            return const.Messages.OPERATION_DONE['ID'], const.Messages.OPERATION_DONE['MESSAGE']

    def ver(self, which: str = 'PRJ', return_type: str = 'SIMPLE_RETURN') -> any:
        """

            Returns modules current version in given type.

            If type was given not correctly function fill return warning in `SIMPLE_RETURN`.

            `which`: str - sets which version you want to get (`DEV`, `PRJ`, `RLS`)
            `return_type`: str - sets type of return (`SIMPLE_RETURN`, `MODULE_RETURN`)

        """
        _ver: str
        if which == 'DEV':
            _ver = const.Settings.DEV_VER
        elif which == 'PRJ':
            _ver = const.Settings.PRJ_VER
        elif which == 'RLS':
            _ver = const.Settings.RLS_VER
        else:
            _ver = const.Warnings.WRONG_WHICH_WHILE_GETTING_VERSION
        
        if return_type == 'SIMPLE_RETURN':
            return _ver
        elif return_type == 'MODULE_RETURN':
            Log.rtn(_ver)
        else:
            return const.Warnings.WRONG_TYPE_WHILE_GETTING_VERSION
        
    def rtn(self, *objects: list) -> const.Settings.Status:
        """

            Main function that takes info from settings You declared in `set` function and returns answer.

            `object`: str - object that you want to return.

            Function returns operations status. Status can be `Error`, `Warning` or simple `Message`.

            By default, status returns to common stream (variable, that takes return info from `rtn` function),
            but you can set this to return status to working place where you wanted to send log in `set` function. 
            If it is cant be done, status will go to common stream.

        """
        const.Settings.LOG_ID += 1

        if const.Settings._ANTI_RECURSION in [0, 1]:
            const.Settings.RETURN_MESSAGE = objects
            const.Settings.RETURN_MESSAGE = list(const.Settings.RETURN_MESSAGE)
            for i in range(len(const.Settings.RETURN_MESSAGE)):
                const.Settings.RETURN_MESSAGE[i] = str(const.Settings.RETURN_MESSAGE[i])

            self.__find_path()

            if const.Settings.RETURN_STATUS_BY_DEFAULT:
                return const.Settings.Status

            elif not const.Settings.RETURN_STATUS_BY_DEFAULT:
                if const.Settings._STANDART_STREAM_RETURN_IF_OPERATION_TYPE_IS_BAD:
                    const.Settings._STANDART_STREAM_RETURN_IF_OPERATION_TYPE_IS_BAD = False

                    return const.Settings.Status
                else:
                    const.Settings._ANTI_RECURSION += 1
                    self.rtn(const.Settings.Status.ID, const.Settings.Status.MESSAGE)
        else:
            const.Settings._ANTI_RECURSION = False

    def __find_path(self, ):
        # Изменить условия на словарь с функциями на месте значений ключей:
        if const.Settings.RETURN_TYPE == 'DEV_CONSOLE':
            for object in const.Settings.RETURN_MESSAGE:
                print(object)
            const.Settings.Status.ID = const.Messages.OPERATION_DONE['ID']
            const.Settings.Status.MESSAGE = const.Messages.OPERATION_DONE['MESSAGE']
        elif const.Settings.RETURN_TYPE == 'TXT':
            const.Settings.Status.ID, const.Settings.Status.MESSAGE = self.__txt()
        elif const.Settings.RETURN_TYPE == 'JSON':
            const.Settings.Status.ID, const.Settings.Status.MESSAGE = self.__json()
        elif const.Settings.RETURN_TYPE == 'HTTP':
            const.Settings.Status.ID, const.Settings.Status.MESSAGE = self.__http()
        else:
            # Если тип файла указан неправильно, делается возврат значения в стандартный поток (переменная):
            if not const.Settings.RETURN_STATUS_BY_DEFAULT:
                const.Settings._STANDART_STREAM_RETURN_IF_OPERATION_TYPE_IS_BAD = True

            const.Settings.Status.ID = const.Warnings.WRONG_TYPE_WHILE_RETURNING['ID']
            const.Settings.Status.MESSAGE = const.Warnings.WRONG_TYPE_WHILE_RETURNING['MESSAGE']


def main():
    """
    
        Dont call this function, because it cant be called as main.

    """
    
    return const.Errors.ACTIVATED_AS_MAIN

if '__name__' == '__main__':
    main()
