items = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover
iteritems = items.items() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/30418481/error-dict-object-has-no-attribute-iteritems
from l3.Runtime import _l_
try:
    _l_(3410)

    iteritems
    _l_(3407)
except NameError:
    _l_(3409)

    iteritems = items
    _l_(3408)

