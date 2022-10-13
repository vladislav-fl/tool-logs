# Logs Helper

Tool that helps You to collect all logs in one place.

# Info:

    All operations returns `status` as Status class. That means that if operation was OK, it will return `Message` otherwise it will return `Error` or `Warning`.

# Import:

    1. from logs import Log
    2. from logs import Log, Settings # If you want to use Settings.Status

# Create class object:

    log: Log = Log(<settings>)

# You can start:

    Choose one of some types:
    
    status: Settings.Status = log.txt(<settings>)
    status: Settings.Status = log.json(<settings>)
    status: Settings.Status = log.http(<settings>)

    etc.
    
# Project TimeLine:

    0.0.1         9 October 2022
    0.0.1.2       9 October 2022

    0.0.2         9 October 2022
    0.0.2.1       10 October 2022
    0.0.2.2       10 October 2022
    0.0.2.3       10 October 2022
    
    0.0.3         10 October 2022

    0.0.4         11 October 2022
    0.0.4.1       11 October 2022

    0.1.0         13 October 2022
    # Some info about 0.1.0:
        Changed full Log class, so now its easier to use it - 
            instead of set, rtn etc. functions its way more easy to use directly http, txt, print etc. functions
        Made more really required constants and delete 'trash' info and constants.
        Provided some more functions like set_id_to_one, check_settings and more.
        Added test.py to test whole project.
        
        Going to add program stream and some info to functions for helping to work with this module

    0.1.1         13 October 2022

    0.9.0         13 October 2022
    # Some info about 0.9.0:
        Almost all functions (only program function left) are ready to go
        test.py is ready to go (only program function left)
        All work in 0.9.0 version will be on LOGS_CONSOLE and program function and it will probably be ready for full user-experience!
