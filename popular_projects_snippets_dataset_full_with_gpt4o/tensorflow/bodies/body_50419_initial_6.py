import numpy as np # pragma: no cover

dtype = None # pragma: no cover
backend = type('MockBackend', (object,), {'floatx': lambda: np.float32 })() # pragma: no cover
dtypes = type('MockDtypes', (object,), {'as_dtype': np.dtype })() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
from l3.Runtime import _l_
if dtype is None:
    _l_(21768)

    dtype = backend.floatx()
    _l_(21767)
aux = dtypes.as_dtype(dtype)
_l_(21769)
exit(aux)
