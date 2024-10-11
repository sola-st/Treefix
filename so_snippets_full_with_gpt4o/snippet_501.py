# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/30418481/error-dict-object-has-no-attribute-iteritems
from l3.Runtime import _l_
try:
    _l_(13749)

    iteritems
    _l_(13746)
except NameError:
    _l_(13748)

    iteritems = items
    _l_(13747)

