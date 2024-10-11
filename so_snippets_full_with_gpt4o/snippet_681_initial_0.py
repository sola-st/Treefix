my_str = '  This  is a  sample   string with  irregular    whitespace.  ' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
from l3.Runtime import _l_
try:
    import re
    _l_(14087)

except ImportError:
    pass

_RE_COMBINE_WHITESPACE = re.compile(r"\s+")
_l_(14088)

my_str = _RE_COMBINE_WHITESPACE.sub(" ", my_str).strip()
_l_(14089)
try:
    import re
    _l_(14091)

except ImportError:
    pass

_RE_COMBINE_WHITESPACE = re.compile(r"(?a:\s+)")
_l_(14092)
_RE_STRIP_WHITESPACE = re.compile(r"(?a:^\s+|\s+$)")
_l_(14093)

my_str = _RE_COMBINE_WHITESPACE.sub(" ", my_str)
_l_(14094)
my_str = _RE_STRIP_WHITESPACE.sub("", my_str)
_l_(14095)

