# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3278077/difference-between-getattr-and-getattribute
from l3.Runtime import _l_
class SomeObject(object):
    _l_(14261)

    pass
    _l_(14260)

class SubObject(SomeObject):
    _l_(14263)

    pass
    _l_(14262)

class SomeObject:
    _l_(14265)

    pass
    _l_(14264)

