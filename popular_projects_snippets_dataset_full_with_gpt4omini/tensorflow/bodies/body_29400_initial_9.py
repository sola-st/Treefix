import numpy as np # pragma: no cover

self = type('Mock', (object,), {'evaluate': lambda x: (x[0].numpy(), x[1].numpy()), 'assertEqual': lambda self, a, b: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
from l3.Runtime import _l_
x = np.random.randint(2, high=10, size=7000)
_l_(10002)
y, idx = array_ops.unique(x)
_l_(10003)
tf_y, tf_idx = self.evaluate([y, idx])
_l_(10004)

self.assertEqual(len(x), len(tf_idx))
_l_(10005)
self.assertEqual(len(tf_y), len(np.unique(x)))
_l_(10006)
for i in range(len(x)):
    _l_(10008)

    self.assertEqual(x[i], tf_y[tf_idx[i]])
    _l_(10007)
