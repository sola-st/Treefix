import numpy as np # pragma: no cover

self = type('Mock', (object,), { # pragma: no cover
    'assertAllEqual': lambda self, a, b: np.testing.assert_array_equal(a, b), # pragma: no cover
    'evaluate': lambda self, v: v.numpy() # pragma: no cover
})() # pragma: no cover

import numpy as np # pragma: no cover

array_ops = type('Mock', (object,), {'ones': lambda shape: tf.ones(shape)})() # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'assertAllEqual': lambda self, a, b: np.testing.assert_array_equal(a, b), # pragma: no cover
    'evaluate': lambda self, v: v.numpy() if tf.is_tensor(v) else v # pragma: no cover
})() # pragma: no cover

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
