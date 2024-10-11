import numpy as np # pragma: no cover
class MockBackend: # pragma: no cover
    def floatx(self): # pragma: no cover
        return 'float32' # pragma: no cover
class MockDtypes: # pragma: no cover
    @staticmethod # pragma: no cover
    def as_dtype(dtype): # pragma: no cover
        return np.dtype(dtype) # pragma: no cover

dtype = None # pragma: no cover
backend = MockBackend() # pragma: no cover
dtypes = MockDtypes() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
from l3.Runtime import _l_
if dtype is None:
    _l_(9424)

    dtype = backend.floatx()
    _l_(9423)
aux = dtypes.as_dtype(dtype)
_l_(9425)
exit(aux)
