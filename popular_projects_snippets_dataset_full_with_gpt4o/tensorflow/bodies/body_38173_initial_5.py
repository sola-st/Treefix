import numpy as np # pragma: no cover

real = np.array([1.0, 2.0, 3.0]) # pragma: no cover
imag = np.array([0.5, 1.5, 2.5]) # pragma: no cover
use_gpu = False # pragma: no cover
test_util = type('Mock', (object,), {'device': lambda self, use_gpu: tf.device('/GPU:0' if use_gpu else '/CPU:0')})() # pragma: no cover
self = type('Mock', (object,), {'evaluate': lambda self, x: x.numpy(), 'assertAllEqual': lambda self, x, y: None, 'assertShapeEqual': lambda self, x, y: None})() # pragma: no cover

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
