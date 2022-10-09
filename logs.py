import staff.logic as logic
import staff.const as const

# Нужно переместить константы в поле экземпляров класса из внешнего чтобы каждый экземпляр работал со своими константами
# То есть, общие константы (версия, стабильность) будут у всех объектов одинаковые, а тип вывода и путь свои для каждого

class Log:
    """

        Main class for working with Logs.

    """
    
    def set(self, ):
        """
        
            Makes start changes where You should set type of answers, path etc.
            
            Call this function at the beginning and each type you want to change settings.
        
        """
        
        pass

    def ver(self, which: str = 'PRJ', return_type: str = 'SIMPLE_RETURN') -> str:
        """

            Returns modules current version in given type.

            If type was given not correctly function fill return warning in SIMPLE_RETURN.

            which: str - sets which version you want to get (DEV, PRJ, RLS)
            return_type: str - sets type of return (SIMPLE_RETURN, MODULE_RETURN)

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
        
    def rtn(self, object: str):
        """

            Main function that takes info from settings You declared in set-function and returns answer.

            object: str - object that you want to return.

        """

        if const.Settings.RETURN_TYPE == 'DEV_CONSOLE':
            print(object)
        else:
            pass
    

def main():
    """
    
        Dont call this function, because it cant be called as main.

    """
    
    return const.Errors.ACTIVATED_AS_MAIN

if '__name__' == '__main__':
    main()
