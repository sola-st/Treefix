ksize = [1, 2, 2, 1] # pragma: no cover
strides = [1, 2, 2, 1] # pragma: no cover
self = type('Mock', (object,), {'assertAllEqual': lambda self, a, b: print('Test Passed' if (tf.reduce_all(a == b).numpy()) else 'Test Failed'), 'evaluate': lambda self, x: x})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
from l3.Runtime import _l_
x = array_ops.ones([3, 6, 5])
_l_(5902)
ksize = 2
_l_(5903)
strides = 2
_l_(5904)

y1 = nn_ops.max_pool_v2(x, ksize, strides, "SAME")
_l_(5905)
y2 = nn_ops.max_pool1d(x, ksize, strides, "SAME")
_l_(5906)

self.assertAllEqual(self.evaluate(y1), self.evaluate(y2))
_l_(5907)
