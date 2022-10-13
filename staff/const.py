class Settings:
    _DEV                 = True
    _DEV_VER_CURRENT     = '0.9.0'
    _DEV_VER_STABLE      = '0.1.1'

    _RLS                 = False
    _RLS_VER_CURRENT     = '0.0'
    _RLS_VER_STABLE      = '0.0'

    # Constants that should be set from the beginning (otherwise they will be set by default):
    
    # DEV_CONSOLE - None, TXT - {PATH-TO-TXT-FILE}, JSON - {PATH_TO_JSON_FILE}, SYSTEM - {PATH_TO_CONSOLE_OR_ANOTHER_PROGRAM_THAT_WILL_DISPLAY_MESSAGES}, HTTP - {HTTP_ADDRESS}:
    def __init__(self, ) -> None:
        pass

    STREAM_TYPE              = 'DEV_CONSOLE'
    STREAM_PATH              = None
    STREAM_LOG               = ''

    LOG_ID                   = 1

    PREFIX_TYPE              = 'NONE'
    PREFIX                   = ''
    RETURN_STATUS            = True
    
    class Status:
        ID                   = 0
        MESSAGE             = ''




# All Errors and Warnings returns simple messages and use only for production and own usage inside console etc.
class Errors:
    ACTIVATED_AS_MAIN                    = {'ID': 10, 'MESSAGE': 'This tool should be used inside another projects. Dont activate it as main project'}
    HTTP_RETURNED_BAD_STATUS             = {'ID': 11, 'MESSAGE': 'HTTP you tried to send log returned bad status'}

    CANT_OPEN_TXT_FILE                   = {'ID': 13, 'MESSAGE': 'Cant open provided txt file. Check <path> and try again'}
    CANT_OPEN_JSON_FILE                  = {'ID': 14, 'MESSAGE': 'Cant open provided json file. Check <path> and try again'}

    ERROR_WHILE_STREAMING_IN_PROGRAM     = {'ID': 15, 'MESSAGE': 'Error accured while streaming in program. Program returned: '}


class Warnings:
    WRONG_WHICH_WHILE_GETTING_VERSION    = {'ID': 20, 'MESSAGE': 'Cant get version because of wrong <which> variable. Check data and call this command again.'}
    WRONG_TYPE_WHILE_GETTING_VERSION     = {'ID': 21, 'MESSAGE': 'Cant get version because of wrong <type> variable. Check data and call this command again'}
    WRONG_TYPE_WHILE_RETURNING           = {'ID': 22, 'MESSAGE': 'Cant return message to stream because <return_type> variable is wrong. Change it and try again'}

    WRONG_PREFIX_TYPE_WHILE_STREAMING    = {'ID': 23, 'MESSAGE': 'Given <prefix_type> is wrong. Check it and try again'}


class Messages:
    OPERATION_DONE                       = {'ID': 30, 'MESSAGE': 'Operation done'}
