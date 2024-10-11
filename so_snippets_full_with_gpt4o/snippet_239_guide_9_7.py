import sys # pragma: no cover

sys.version_info = (2, 7, 18) # pragma: no cover
value = b'test_string' # pragma: no cover
six = type('Mock', (object,), {'string_types': (str,)}) # pragma: no cover
basestring = str # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
from l3.Runtime import _l_
try:
    import six
    _l_(13410)

except ImportError:
    pass

if isinstance(value, six.string_types):
    _l_(13412)

    pass # It's a string !!
    _l_(13411) # It's a string !!
try:
    import sys
    _l_(13414)

except ImportError:
    pass

PY3 = sys.version_info[0] == 3
_l_(13415)

if PY3:
    _l_(13418)

    string_types = str,
    _l_(13416)
else:
    string_types = basestring,
    _l_(13417)

