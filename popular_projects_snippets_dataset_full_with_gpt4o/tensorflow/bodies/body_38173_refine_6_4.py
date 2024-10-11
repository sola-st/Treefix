import numpy as np # pragma: no cover

real = np.array([1.0, 2.0, 3.0]) # pragma: no cover
imag = np.array([1.0, 0.5, 0.0]) # pragma: no cover
test_util = type('Mock', (object,), {'device': lambda use_gpu: type('DeviceContext', (object,), {'__enter__': lambda self: None, '__exit__': lambda self, exc_type, exc_val, exc_tb: None})()})() # pragma: no cover
use_gpu = False # pragma: no cover
self = type('Mock', (object,), {'evaluate': lambda self, x: x.numpy(), 'assertAllEqual': np.testing.assert_allclose, 'assertShapeEqual': lambda np_ans, tf_ans: np.testing.assert_array_equal(np_ans.shape, tf_ans.shape)})() # pragma: no cover

import numpy as np # pragma: no cover

real = np.array([1.0, 2.0, 3.0]) # pragma: no cover
imag = np.array([4.0, 5.0, 6.0]) # pragma: no cover
class MockDeviceContextManager:# pragma: no cover
    def __init__(self, use_gpu):# pragma: no cover
        self.use_gpu = use_gpu# pragma: no cover
    def __enter__(self):# pragma: no cover
        return self# pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb):# pragma: no cover
        pass# pragma: no cover
 # pragma: no cover
test_util = type('Mock', (object,), {'device': lambda self, use_gpu: MockDeviceContextManager(use_gpu)})() # pragma: no cover
use_gpu = False # pragma: no cover
class MockOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def convert_to_tensor(x):# pragma: no cover
        return tf.convert_to_tensor(x, dtype=tf.float32)# pragma: no cover
 # pragma: no cover
ops = MockOps() # pragma: no cover
class MockMathOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def complex(real, imag):# pragma: no cover
        return tf.complex(real, imag)# pragma: no cover
 # pragma: no cover
math_ops = MockMathOps() # pragma: no cover
class MockSelf:# pragma: no cover
    def evaluate(self, tensor):# pragma: no cover
        return tensor.numpy()# pragma: no cover
    def assertAllEqual(self, a, b):# pragma: no cover
        np.testing.assert_array_equal(a, b)# pragma: no cover
    def assertShapeEqual(self, a, b):# pragma: no cover
        assert a.shape == b.shape, f'Shapes do not match: {a.shape} vs {b.shape}'# pragma: no cover
 # pragma: no cover
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
