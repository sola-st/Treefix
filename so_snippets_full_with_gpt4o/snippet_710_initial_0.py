import random # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7585307/how-to-correct-typeerror-unicode-objects-must-be-encoded-before-hashing
from l3.Runtime import _l_
try:
    import hashlib
    _l_(13850)

except ImportError:
    pass
hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
_l_(13851)
'cd183a211ed2434eac4f31b317c573c50e6c24e3a28b82ddcb0bf8bedf387a9f'
_l_(13852)

