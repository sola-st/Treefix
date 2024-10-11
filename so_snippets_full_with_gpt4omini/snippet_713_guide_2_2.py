import sys # pragma: no cover
import datetime # pragma: no cover

class MockUtils: pass # pragma: no cover
class MockTimezone: pass # pragma: no cover
sys.modules['django'] = type('Mock', (object,), {'utils': MockUtils()})() # pragma: no cover
sys.modules['django'].utils.timezone = MockTimezone() # pragma: no cover
sys.modules['django'].utils.timezone.now = staticmethod(lambda: datetime.datetime(2023, 10, 1, 12, 0, 0)) # pragma: no cover
now_aware = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/796008/cant-subtract-offset-naive-and-offset-aware-datetimes
from l3.Runtime import _l_
try:
    from django.utils import timezone
    _l_(2338)

except ImportError:
    pass
now_aware = timezone.now()
_l_(2339)

