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
    RETURN_TYPE              = 'DEV_CONSOLE'
    RETURN_PATH              = None
    TEST                     = False
    RETURN_STATUS_BY_DEFAULT = True

    OPERATION_STATUS         = ''



# All Errors and Warnings returns simple messages and use only for production and own usage inside console etc.
class Errors:
    ACTIVATED_AS_MAIN                    = {'STATUS ID': 10, 'STATUS MESSAGE': 'This tool should be used inside another projects. Dont activate it as main project.'}
    HTTP_RETURNED_BAD_STATUS             = {'STATUS ID': 11, 'STATUS MESSAGE': 'HTTP you tried to send log returned bad status'}


class Warnings:
    WRONG_WHICH_WHILE_GETTING_VERSION    = {'STATUS ID': 20, 'STATUS MESSAGE': 'Cant get version because of wrong <which> variable. Check data and call this command again.'}
    WRONG_TYPE_WHILE_GETTING_VERSION     = {'STATUS ID': 21, 'STATUS MESSAGE': 'Cant get version because of wrong <type> variable. Check data and call this command again'}


class Messages:
    OPERATION_DONE                       = {'STATUS ID': 30, 'STATUS MESSAGE': 'Operation done.'}
