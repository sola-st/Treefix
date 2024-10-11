import numpy as np # pragma: no cover
from unittest.mock import Mock # pragma: no cover

test = Mock() # pragma: no cover
test.is_gpu_available = Mock(return_value=False) # pragma: no cover
self = Mock() # pragma: no cover
self.skipTest = Mock() # pragma: no cover
np.float16 = np.dtype('float16') # pragma: no cover
np.float32 = np.dtype('float32') # pragma: no cover
np.float64 = np.dtype('float64') # pragma: no cover
dtypes = Mock() # pragma: no cover
dtypes.bfloat16 = Mock() # pragma: no cover
dtypes.bfloat16.as_numpy_dtype = np.dtype('float16') # pragma: no cover
self._testCrelu = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
from l3.Runtime import _l_
if not test.is_gpu_available():
    _l_(9332)

    self.skipTest("No GPU available")
    _l_(9331)
for t in [
    np.float16,
    np.float32,
    np.float64,
    dtypes.bfloat16.as_numpy_dtype,
]:
    _l_(9334)

    self._testCrelu(
        np.array([[-9, 7, -5, 3, -1], [1, -3, 5, -7, 9]]).astype(t))
    _l_(9333)
