import numpy as np # pragma: no cover

real = np.array([1.0, 2.0, 3.0]) # pragma: no cover
imag = np.array([0.5, 0.25, 0.75]) # pragma: no cover
use_gpu = False # pragma: no cover
self = type('Mock', (object,), {'evaluate': lambda self, x: x.numpy(), 'assertAllEqual': lambda self, a, b: np.testing.assert_array_equal(a, b), 'assertShapeEqual': lambda self, a, b: self.assertEqual(a.shape, b.shape)})() # pragma: no cover

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
