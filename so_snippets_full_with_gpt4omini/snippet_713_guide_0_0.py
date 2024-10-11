class Mock(object): # pragma: no cover
    def now(): # pragma: no cover
        return '2023-10-01T12:00:00Z' # pragma: no cover

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

