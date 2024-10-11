nn_ops = type('Mock', (), {'max_pool_v2': staticmethod(lambda x, ksize, strides, padding: tf.nn.max_pool(x, ksize=[1, ksize, ksize, 1], strides=[1, strides, strides, 1], padding=padding)), 'max_pool1d': staticmethod(lambda x, ksize, strides, padding: tf.nn.max_pool1d(x, ksize=ksize, strides=strides, padding=padding))})() # pragma: no cover
ksize = 2 # pragma: no cover
strides = 2 # pragma: no cover

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
