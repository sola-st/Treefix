import numpy as np # pragma: no cover

real = np.array([1.0, 2.0, 3.0]) # pragma: no cover
imag = np.array([4.0, 5.0, 6.0]) # pragma: no cover
use_gpu = False # pragma: no cover
test_util = type('MockTestUtil', (object,), {'device': lambda self, use_gpu: (lambda x: x)()})() # pragma: no cover
self = type('Mock', (object,), {'evaluate': lambda self, x: x.numpy(), 'assertAllEqual': lambda a, b: print('Assert All Equal:', np.array_equal(a, b)), 'assertShapeEqual': lambda a, b: print('Assert Shape Equal:', a.shape == b.shape)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
from l3.Runtime import _l_
np_ans = real + (1j) * imag
_l_(4079)

with test_util.device(use_gpu=use_gpu):
    _l_(4084)

    real = ops.convert_to_tensor(real)
    _l_(4080)
    imag = ops.convert_to_tensor(imag)
    _l_(4081)
    tf_ans = math_ops.complex(real, imag)
    _l_(4082)
    out = self.evaluate(tf_ans)
    _l_(4083)

self.assertAllEqual(np_ans, out)
_l_(4085)
self.assertShapeEqual(np_ans, tf_ans)
_l_(4086)
