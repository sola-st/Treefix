# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/432112/is-there-a-numpy-function-to-return-the-first-index-of-something-in-an-array
from l3.Runtime import _l_
sequence_of_arrays = [[0, 1], [1, 2], [-5, 0]]
_l_(12211)
arrays_to_query = [[-5, 0], [1, 0]]
_l_(12212)
try:
    import numpy_indexed as npi
    _l_(12214)

except ImportError:
    pass
idx = npi.indices(sequence_of_arrays, arrays_to_query, missing=-1)
_l_(12215)
print(idx)   # [2, -1]
_l_(12216)   # [2, -1]

