import binascii # pragma: no cover

value = binascii.unhexlify('48656c6c6f20576f726c6421') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = value.hex
_l_(5077)
exit(aux)
