text = 'Hello' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1228299/changing-one-character-in-a-string
from l3.Runtime import _l_
new = text[:1] + 'Z' + text[2:]
_l_(13857)

