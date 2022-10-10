class Settings:
    DEV         = True
    DEV_VER     = '0.0.2.3'
    DEV_STABLE  = True

    PRJ         = 'DEV'
    PRJ_VER     = DEV_VER
    PRJ_STABLE  = True

    RLS         = False
    RLS_VER     = '0.0.0'
    RLS_STABLE  = False

    # Constants that should be set from the beginning (otherwise they will be set by default):
    
    # DEV_CONSOLE - None, TXT - {PATH-TO-TXT-FILE}, JSON - {PATH_TO_JSON_FILE}, SYSTEM - {PATH_TO_CONSOLE_OR_ANOTHER_PROGRAM_THAT_WILL_DISPLAY_MESSAGES}, HTTP - {HTTP_ADDRESS}:
    RETURN_TYPE = 'DEV_CONSOLE'
    RETURN_PATH = None



# All Errors and Warnings returns simple messages and use only for production and own usage inside console etc.
class Errors:
    ACTIVATED_AS_MAIN                    = 'This tool should be used inside another projects. Dont activate it as main project.'


class Warnings:
    WRONG_WHICH_WHILE_GETTING_VERSION    = 'Cant get version because of wrong <which> variable. Check data and call this command again.'
    WRONG_TYPE_WHILE_GETTING_VERSION     = 'Cant get version because of wrong <type> variable. Check data and call this command again'


class Messages:
    OPERATION_DONE                       = 'Operation done.'
