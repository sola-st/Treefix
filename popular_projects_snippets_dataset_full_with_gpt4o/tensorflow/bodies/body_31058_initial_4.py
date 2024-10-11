import numpy as np # pragma: no cover

test = type('Mock', (object,), {'is_gpu_available': lambda: False})() # pragma: no cover
self = type('Mock', (object,), {'skipTest': lambda self, message: print(message), '_testCrelu': lambda self, array: print(array)})() # pragma: no cover
dtypes = type('Mock', (object,), {'bfloat16': type('Mock', (object,), {'as_numpy_dtype': np.float32})})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
from l3.Runtime import _l_
if not test.is_gpu_available():
    _l_(21650)

    self.skipTest("No GPU available")
    _l_(21649)
for t in [
    np.float16,
    np.float32,
    np.float64,
    dtypes.bfloat16.as_numpy_dtype,
]:
    _l_(21652)

    self._testCrelu(
        np.array([[-9, 7, -5, 3, -1], [1, -3, 5, -7, 9]]).astype(t))
    _l_(21651)
