import staff.logic as logic
import staff.const as const

import logging
import json

# Нужно переместить константы в поле экземпляров класса из внешнего чтобы каждый экземпляр работал со своими константами
# То есть, общие константы (версия, стабильность) будут у всех объектов одинаковые, а тип вывода и путь свои для каждого

# Добавить вариант нескольких потоков выхода - Check
# В аргументах set функции у аргумента return_path указать не любые принимаемые данные, а конкретно bool или str (ну или еще что то, если додумаюсь :))

# Перенести всю логику программы (ключевые функции, а возможно и сам класс в logic.py)

# Сделать возврат какого-либо ответа от каждой функции после вызова ver, set, rtn и тд (подумать, нужно ли)

# Установить проверку добавления данных в JSON (чтобы были пары ключ - значение)
# Добавить в json добавление не просто текста, а данных в существующий словарь, либо его создание

class Log:
    """

        Main class for working with Logs.

    """
    
    def __txt(self, ):
        with open(const.Settings.RETURN_PATH, 'a') as txt_file:
            for object in self.objects:
                txt_file.write(object + '\n')
            txt_file.close()

    def __json(self, ):
        with open(const.Settings.RETURN_PATH, 'a') as json_file:
            for object in self.objects:
                json.dump(object, json_file)
            json_file.close()

    def __http(self, ):
        pass
    
    def set(self, return_type: str = 'DEV_CONSOLE', return_path: any = None):
        """
        
            Makes start changes where You should set type of output stream, output path etc.
            
            Call this function at the beginning and each time you want to change settings.

            Commonly `rtn` function will return objects to the common stream (in which would return `print` function) if return type is not given.
        
            Commonly `return_path` is None because `return_type` is `DEV_CONSOLE` if nothing is given. 
            You should give path to the file if you are going to use `TXT`, `JSON` etc. as output stream.

            If You want, there is opportunity not to use set function and leave all constants as they are.

        """
        const.Settings.RETURN_TYPE = return_type
        const.Settings.RETURN_PATH = return_path
        pass

    def ver(self, which: str = 'PRJ', return_type: str = 'SIMPLE_RETURN') -> str:
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
        
    def rtn(self, *objects: list):
        """

            Main function that takes info from settings You declared in `set` function and returns answer.

            `object`: str - object that you want to return.

        """
        self.objects = objects
        for object in self.objects:
            object = str(object)

        # Изменить условия на словарь с функциями на месте значений ключей:
        if const.Settings.RETURN_TYPE == 'DEV_CONSOLE':
            for object in self.objects:
                print(object)
        elif const.Settings.RETURN_TYPE == 'TXT':
            self.__txt()
        elif const.Settings.RETURN_TYPE == 'JSON':
            self.__json()
        elif const.Settings.RETURN_TYPE == 'HTTP':
            self.__http()
        else:
            pass
    

def main():
    """
    
        Dont call this function, because it cant be called as main.

    """
    
    return const.Errors.ACTIVATED_AS_MAIN

if '__name__' == '__main__':
    main()
