import sys # pragma: no cover
import types # pragma: no cover

schedule = types.ModuleType('schedule') # pragma: no cover
time = types.ModuleType('time') # pragma: no cover
schedule.every = lambda interval=1: type('MockJob', (object,), { # pragma: no cover
    'minutes': lambda self, job: None, # pragma: no cover
    'hour': lambda self, job: None, # pragma: no cover
    'day': lambda self: type('DayMock', (object,), {'at': lambda self, time: None})(), # pragma: no cover
    'do': lambda self, job: None # pragma: no cover
})() # pragma: no cover
schedule.run_pending = lambda: None # pragma: no cover
time.sleep = lambda s: None # pragma: no cover
sys.modules['schedule'] = schedule # pragma: no cover
sys.modules['time'] = time # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/373335/how-do-i-get-a-cron-like-scheduler-in-python
from l3.Runtime import _l_
try:
    import schedule
    _l_(14249)

except ImportError:
    pass
try:
    import time
    _l_(14251)

except ImportError:
    pass

def job():
    _l_(14253)

    print("I'm working...")
    _l_(14252)

schedule.every(10).minutes.do(job)
_l_(14254)
schedule.every().hour.do(job)
_l_(14255)
schedule.every().day.at("10:30").do(job)
_l_(14256)

while 1:
    _l_(14259)

    schedule.run_pending()
    _l_(14257)
    time.sleep(1)
    _l_(14258)

