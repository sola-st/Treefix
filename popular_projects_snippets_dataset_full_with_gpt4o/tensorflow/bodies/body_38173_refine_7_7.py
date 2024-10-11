import numpy as np # pragma: no cover

real = np.array([1.0, 2.0, 3.0]) # pragma: no cover
imag = np.array([0.5, 1.5, 2.5]) # pragma: no cover
test_util = type('Mock', (object,), {'device': lambda self, use_gpu: lambda: None})() # pragma: no cover
use_gpu = False # pragma: no cover
self = type('Mock', (object,), {'evaluate': lambda self, x: x.numpy(), 'assertAllEqual': lambda self, x, y: np.testing.assert_array_equal(x, y), 'assertShapeEqual': lambda self, x, y: None})() # pragma: no cover

import numpy as np # pragma: no cover

real = np.array([1.0, 2.0, 3.0], dtype=np.float32) # pragma: no cover
imag = np.array([4.0, 5.0, 6.0], dtype=np.float32) # pragma: no cover
use_gpu = False # pragma: no cover
class MockDevice(object):# pragma: no cover
    def __init__(self, use_gpu):# pragma: no cover
        self.use_gpu = use_gpu# pragma: no cover
    def __enter__(self):# pragma: no cover
        pass# pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb):# pragma: no cover
        pass # pragma: no cover
test_util = type('Mock', (object,), {'device': lambda self, use_gpu: MockDevice(use_gpu)})() # pragma: no cover
ops = type('Mock', (object,), {'convert_to_tensor': lambda x: tf.convert_to_tensor(x, dtype=tf.float32)})() # pragma: no cover
class MockSelf(object):# pragma: no cover
    def evaluate(self, tensor):# pragma: no cover
        return tensor.numpy()# pragma: no cover
    def assertAllEqual(self, a, b):# pragma: no cover
        np.testing.assert_allclose(a, b)# pragma: no cover
    def assertShapeEqual(self, np_array, tf_tensor):# pragma: no cover
        assert np_array.shape == tf_tensor.shape, f'Shapes do not match: {np_array.shape} vs {tf_tensor.shape}' # pragma: no cover
self = MockSelf() # pragma: no cover

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
