import numpy as np # pragma: no cover

class Mock: # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        with tf.compat.v1.Session() as sess: # pragma: no cover
            return sess.run(tensor) # pragma: no cover
 # pragma: no cover
    def assertAllEqual(self, a, b): # pragma: no cover
        a_val, b_val = self.evaluate(a), self.evaluate(b) # pragma: no cover
        np.testing.assert_array_equal(a_val, b_val) # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
from l3.Runtime import _l_
x = array_ops.ones([3, 6, 5])
_l_(17657)
ksize = 2
_l_(17658)
strides = 2
_l_(17659)

y1 = nn_ops.max_pool_v2(x, ksize, strides, "SAME")
_l_(17660)
y2 = nn_ops.max_pool1d(x, ksize, strides, "SAME")
_l_(17661)

self.assertAllEqual(self.evaluate(y1), self.evaluate(y2))
_l_(17662)
