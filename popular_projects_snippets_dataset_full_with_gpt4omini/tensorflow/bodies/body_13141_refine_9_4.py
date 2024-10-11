nn_ops = type('Mock', (object,), {'max_pool_v2': lambda x, k, s, p: tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, s, s, 1], padding=p), 'max_pool1d': lambda x, k, s, p: tf.nn.pool(x, window_shape=[k], pooling_type='MAX', strides=[s], padding=p)})() # pragma: no cover
self = type('Mock', (object,), {'assertAllEqual': lambda self, a, b: print('Assert All Equal:', a == b), 'evaluate': lambda self, x: x})() # pragma: no cover

class Mock: # pragma: no cover
    def assertAllEqual(self, a, b): # pragma: no cover
        assert (a == b).all() # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        return tensor.numpy() if isinstance(tensor, tf.Tensor) else tensor # pragma: no cover
self = Mock() # pragma: no cover

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
