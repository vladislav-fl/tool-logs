# Logs Helper

Tool that helps You to collect all logs in one place.

# Info:

    All operations returns `status` as Status class. That means that if operation was OK, it will return `Message` otherwise it will return `Error` or `Warning`.

    BUT:
        Function `ver` will return module version to choosen stream if operation was OK.

# Import:

    1. from logs import Log
    2. import logs # so you will have to use logs.Log 

# Create class object:

    <var_name> = Log()

# Set up object (if you need to):

    If you are sure that connection will be OK, you can use:
    
    <var_name>.set(<settings>), that will set settings for next connections without testing it.

    Otherwise, you will want to use this:

    <var_name>.set(<settings>, test = True), that will set settings for next connections with testing it.

# You can start:

    Call rtn function to start streaming process

    <var_name>.rtn(<settings>)
    
# TimeLine

    0.0.1     |   9 October 2022
    0.0.1.2   |   9 October 2022

    0.0.2     |   9 October 2022
    0.0.2.1   |   10 October 2022
    0.0.2.2   |   10 October 2022
    0.0.2.3   |   10 October 2022
    
    0.0.3     |   10 October 2022
