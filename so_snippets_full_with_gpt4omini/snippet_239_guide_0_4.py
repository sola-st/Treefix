import sys # pragma: no cover
import six # pragma: no cover

value = 'example string' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
from l3.Runtime import _l_
try:
    import six
    _l_(1696)

except ImportError:
    pass

if isinstance(value, six.string_types):
    _l_(1698)

    pass # It's a string !!
    _l_(1697) # It's a string !!
try:
    import sys
    _l_(1700)

except ImportError:
    pass

PY3 = sys.version_info[0] == 3
_l_(1701)

if PY3:
    _l_(1704)

    string_types = str,
    _l_(1702)
else:
    string_types = basestring,
    _l_(1703)

