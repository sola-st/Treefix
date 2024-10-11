b = 'some string' # pragma: no cover
unicode = str # pragma: no cover
def do_something_else(): pass # pragma: no cover
basestring = str # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance
from l3.Runtime import _l_
if isinstance(b, (str, unicode)):
    _l_(2113)

    do_something_else()
    _l_(2112)

if isinstance(b, basestring):
    _l_(2115)

    do_something_else()
    _l_(2114)

