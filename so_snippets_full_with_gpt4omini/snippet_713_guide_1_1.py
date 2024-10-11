import sys # pragma: no cover
from datetime import datetime # pragma: no cover

class Mock: pass # pragma: no cover
sys.modules['django'] = Mock() # pragma: no cover
sys.modules['django'].utils = Mock() # pragma: no cover
sys.modules['django'].utils.timezone = Mock() # pragma: no cover
sys.modules['django'].utils.timezone.now = staticmethod(lambda: datetime(2023, 10, 1, 12, 0, 0)) # pragma: no cover
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

