from logs import Log
from staff.const import Settings

log: Log = Log()



log.set('JSON', 'text.json', True, False, True, True)

for i in range(10):
    status: Settings.Status = log.rtn('LOG - ', i)
    print('[STATUS ID] -', status.ID)
    print('[STATUS MESSAGE] -', status.MESSAGE)
    print('-' * 10)