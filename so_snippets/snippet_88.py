# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
from l3.Runtime import _l_
try:
    from random import randrange
    _l_(1374)

except ImportError:
    pass
print(randrange(10))
_l_(1375)

