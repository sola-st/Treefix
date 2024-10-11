nn_ops = type('Mock', (object,), {'max_pool_v2': lambda x, k, s, p: tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, s, s, 1], padding=p), 'max_pool1d': lambda x, k, s, p: tf.nn.max_pool1d(x, ksize=k, strides=s, padding=p)})() # pragma: no cover
self = type('Mock', (object,), {'assertAllEqual': lambda a, b: tf.reduce_all(tf.equal(a, b)), 'evaluate': lambda x: x})() # pragma: no cover

import numpy as np # pragma: no cover

class MockSelf: # pragma: no cover
    def assertAllEqual(self, a, b): # pragma: no cover
        assert np.array_equal(a, b), 'Values are not equal' # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        return tensor if isinstance(tensor, np.ndarray) else tensor.numpy() # pragma: no cover
self = MockSelf() # pragma: no cover

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
