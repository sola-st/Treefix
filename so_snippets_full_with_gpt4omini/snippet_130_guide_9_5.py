class Mock: pass # pragma: no cover
data = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
from l3.Runtime import _l_
try:
    _l_(1355)

    data=str(data)
    _l_(1352)
except:
    _l_(1354)

    data = data #Don't convert to String
    _l_(1353) #Don't convert to String

