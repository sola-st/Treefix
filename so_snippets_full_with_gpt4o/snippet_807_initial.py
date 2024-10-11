# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename
from l3.Runtime import _l_
try:
    import re
    _l_(15020)

except ImportError:
    pass
t = re.compile("[a-zA-Z0-9.,_-]")
_l_(15021)
unsafe = "abc∂éåß®∆˚˙©¬ñ√ƒµ©∆∫ø"
_l_(15022)
safe = [ch for ch in unsafe if t.match(ch)]
_l_(15023)
try:
    from random import choice
    _l_(15025)

except ImportError:
    pass
try:
    from string import ascii_lowercase, ascii_uppercase, digits
    _l_(15027)

except ImportError:
    pass
allowed_chr = ascii_lowercase + ascii_uppercase + digits
_l_(15028)

safe = ''.join([choice(allowed_chr) for _ in range(16)])
_l_(15029)
# => 'CYQ4JDKE9JfcRzAZ'

