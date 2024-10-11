class Mocktimezone: # pragma: no cover
    @staticmethod # pragma: no cover
    def now(): # pragma: no cover
        return 'mocked time now' # pragma: no cover
 # pragma: no cover

timezone = Mocktimezone # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/796008/cant-subtract-offset-naive-and-offset-aware-datetimes
from l3.Runtime import _l_
try:
    from django.utils import timezone
    _l_(14697)

except ImportError:
    pass
now_aware = timezone.now()
_l_(14698)

