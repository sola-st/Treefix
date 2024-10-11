import sys # pragma: no cover
import types # pragma: no cover

mock_schedule_module = types.ModuleType('schedule') # pragma: no cover
mock_time_module = types.ModuleType('time') # pragma: no cover
sys.modules['schedule'] = mock_schedule_module # pragma: no cover
sys.modules['time'] = mock_time_module # pragma: no cover
class MockJob: # pragma: no cover
    def do(self, job): # pragma: no cover
        job() # pragma: no cover
mock_schedule_module.every = lambda _: MockJob() # pragma: no cover
mock_schedule_module.run_pending = lambda: None # pragma: no cover
mock_time_module.sleep = lambda _: None # pragma: no cover

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

