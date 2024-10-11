import sys # pragma: no cover
class Mock: pass # pragma: no cover

sys.modules['django'] = Mock() # pragma: no cover
sys.modules['django'].utils = Mock() # pragma: no cover
sys.modules['django'].utils.timezone = Mock() # pragma: no cover
def mock_now(): return '2023-10-01 12:00:00' # pragma: no cover
sys.modules['django'].utils.timezone.now = staticmethod(mock_now) # pragma: no cover

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

