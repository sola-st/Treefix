class MockTimezone: # pragma: no cover
    @staticmethod # pragma: no cover
    def now(): # pragma: no cover
        import datetime # pragma: no cover
        return datetime.datetime.now(datetime.timezone.utc) # pragma: no cover

timezone = MockTimezone() # pragma: no cover

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

