from logs import Log, Settings

# new version (recreation)

log: Log = Log()

# TXT LOGGING
#-------------------------------------------------

input('Press Enter to test TXT...\n')
for i in range(5):
    status: Settings.Status = log.txt('text.txt', 'Hello, logs_2!')
    print(status.ID)
    print(status.MESSAGE)

# HTTP LOGGING
#-------------------------------------------------

input('Press Enter to test HTTP...\n')
status: Settings.Status = log.http('https://google.com', 'Hello!')
print(status.ID)
print(status.MESSAGE)

# JSON LOGGING
#-------------------------------------------------

input('Press Enter to test JSON...\n')
status: Settings.Status = log.json('text.json', {'id': 1, 'parameter': 'Hello, World!'})
print(status.ID)
print(status.MESSAGE)

# SIMPLE PRINT LOGGING
#-------------------------------------------------

input('Press Enter to test PRINT...\n')
# Settings LOG_ID to 1:
status = log.set_id_to_one()

status: Settings.Status = log.print('Hello, World!')
print(status.ID)
print(status.MESSAGE)


