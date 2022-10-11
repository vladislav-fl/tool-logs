class Settings:
    DEV         = True
    DEV_VER     = '0.0.4'
    DEV_STABLE  = True

    PRJ         = 'DEV'
    PRJ_VER     = DEV_VER
    PRJ_STABLE  = True

    RLS         = False
    RLS_VER     = '0.0.0'
    RLS_STABLE  = False

    # Constants that should be set from the beginning (otherwise they will be set by default):
    
    # DEV_CONSOLE - None, TXT - {PATH-TO-TXT-FILE}, JSON - {PATH_TO_JSON_FILE}, SYSTEM - {PATH_TO_CONSOLE_OR_ANOTHER_PROGRAM_THAT_WILL_DISPLAY_MESSAGES}, HTTP - {HTTP_ADDRESS}:
    RETURN_TYPE              = 'DEV_CONSOLE'
    RETURN_PATH              = None
    RETURN_MESSAGE           = ''

    TEST                     = False
    RETURN_STATUS_BY_DEFAULT = True

    OPERATION_STATUS         = ''

    _ANTI_RECURSION          = 0
    _STANDART_STREAM_RETURN_IF_OPERATION_TYPE_IS_BAD = False
    
    class Status:
        ID                   = 0
        MESSAGE             = ''




# All Errors and Warnings returns simple messages and use only for production and own usage inside console etc.
class Errors:
    ACTIVATED_AS_MAIN                    = {'ID': 10, 'MESSAGE': 'This tool should be used inside another projects. Dont activate it as main project'}
    HTTP_RETURNED_BAD_STATUS             = {'ID': 11, 'MESSAGE': 'HTTP you tried to send log returned bad status'}


class Warnings:
    WRONG_WHICH_WHILE_GETTING_VERSION    = {'ID': 20, 'MESSAGE': 'Cant get version because of wrong <which> variable. Check data and call this command again.'}
    WRONG_TYPE_WHILE_GETTING_VERSION     = {'ID': 21, 'MESSAGE': 'Cant get version because of wrong <type> variable. Check data and call this command again'}
    WRONG_TYPE_WHILE_RETURNING           = {'ID': 22, 'MESSAGE': 'Cant return message to stream because <return_type> variable is wrong. Change it and try again'}


class Messages:
    OPERATION_DONE                       = {'ID': 30, 'MESSAGE': 'Operation done.'}
