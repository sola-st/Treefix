import numpy as np # pragma: no cover

dtype = np.float32 # pragma: no cover
backend = type('Mock', (object,), {'floatx': lambda: 'float32'})() # pragma: no cover
dtypes = type('Mock', (object,), {'as_dtype': lambda x: tf.dtypes.as_dtype(x)})() # pragma: no cover

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
