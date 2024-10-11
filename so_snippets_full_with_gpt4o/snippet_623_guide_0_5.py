import datetime # pragma: no cover
import sys # pragma: no cover
type('nptime', (object,), {}) # pragma: no cover
from dataclasses import dataclass # pragma: no cover
import types # pragma: no cover

sys.modules['nptime'] = types.ModuleType('nptime') # pragma: no cover
setattr(sys.modules['nptime'], 'nptime', type('nptime', (object,), {'__init__': lambda self, h, m, s: setattr(self, 'time', (h, m, s)), '__add__': lambda self, td: 'Added timedelta to nptime'})) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/100210/what-is-the-standard-way-to-add-n-seconds-to-datetime-time-in-python
from l3.Runtime import _l_
try:
    import datetime
    _l_(15088)

except ImportError:
    pass
try:
    import nptime
    _l_(15090)

except ImportError:
    pass
nptime.nptime(11, 34, 59) + datetime.timedelta(0, 3)
_l_(15091)
nptime(11, 35, 2)
_l_(15092)

