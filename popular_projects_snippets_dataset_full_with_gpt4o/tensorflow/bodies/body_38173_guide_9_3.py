import numpy as np # pragma: no cover

real = np.array([1.0, 2.0, 3.0], dtype=np.float32) # pragma: no cover
imag = np.array([0.5, 1.5, 2.5], dtype=np.float32) # pragma: no cover
use_gpu = False # pragma: no cover
class MockTest: # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        return tensor.numpy() # pragma: no cover
    def assertAllEqual(self, a, b): # pragma: no cover
        np.testing.assert_array_equal(a, b) # pragma: no cover
    def assertShapeEqual(self, a, b): # pragma: no cover
        assert a.shape == b.shape # pragma: no cover
self = MockTest() # pragma: no cover
class DeviceContextManager: # pragma: no cover
    def __init__(self, use_gpu): # pragma: no cover
        self.use_gpu = use_gpu # pragma: no cover
    def __enter__(self): # pragma: no cover
        if self.use_gpu: # pragma: no cover
            print('Using GPU') # pragma: no cover
        else: # pragma: no cover
            print('Using CPU') # pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
        pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
from l3.Runtime import _l_
np_ans = real + (1j) * imag
_l_(15599)

with test_util.device(use_gpu=use_gpu):
    _l_(15604)

    real = ops.convert_to_tensor(real)
    _l_(15600)
    imag = ops.convert_to_tensor(imag)
    _l_(15601)
    tf_ans = math_ops.complex(real, imag)
    _l_(15602)
    out = self.evaluate(tf_ans)
    _l_(15603)

self.assertAllEqual(np_ans, out)
_l_(15605)
self.assertShapeEqual(np_ans, tf_ans)
_l_(15606)
