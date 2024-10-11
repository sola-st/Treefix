# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python
from l3.Runtime import _l_
try:
    import os
    _l_(3210)

except ImportError:
    pass
workers = os.cpu_count()
_l_(3211)
if 'sched_getaffinity' in dir(os):
    _l_(3213)

    workers = len(os.sched_getaffinity(0))
    _l_(3212)

