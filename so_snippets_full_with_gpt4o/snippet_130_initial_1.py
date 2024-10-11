data = 123  # Example integer value # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
from l3.Runtime import _l_
try:
    _l_(13013)

    data=str(data)
    _l_(13010)
except:
    _l_(13012)

    data = data #Don't convert to String
    _l_(13011) #Don't convert to String

