import datetime # pragma: no cover

timezone = type('Mock', (object,), {'now': lambda: datetime.datetime.now(datetime.timezone.utc)})() # pragma: no cover

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

