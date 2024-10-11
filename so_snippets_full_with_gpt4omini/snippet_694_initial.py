# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/373335/how-do-i-get-a-cron-like-scheduler-in-python
from l3.Runtime import _l_
try:
    import schedule
    _l_(1854)

except ImportError:
    pass
try:
    import time
    _l_(1856)

except ImportError:
    pass

def job():
    _l_(1858)

    print("I'm working...")
    _l_(1857)

schedule.every(10).minutes.do(job)
_l_(1859)
schedule.every().hour.do(job)
_l_(1860)
schedule.every().day.at("10:30").do(job)
_l_(1861)

while 1:
    _l_(1864)

    schedule.run_pending()
    _l_(1862)
    time.sleep(1)
    _l_(1863)

