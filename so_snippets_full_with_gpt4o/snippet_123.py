# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance
from l3.Runtime import _l_
if isinstance(b, (str, unicode)):
    _l_(14300)

    do_something_else()
    _l_(14299)

if isinstance(b, basestring):
    _l_(14302)

    do_something_else()
    _l_(14301)

