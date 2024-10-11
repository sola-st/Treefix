import numpy as np # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
from l3.Runtime import _l_
x = np.random.randint(2, high=10, size=7000)
_l_(22291)
y, idx = array_ops.unique(x)
_l_(22292)
tf_y, tf_idx = self.evaluate([y, idx])
_l_(22293)

self.assertEqual(len(x), len(tf_idx))
_l_(22294)
self.assertEqual(len(tf_y), len(np.unique(x)))
_l_(22295)
for i in range(len(x)):
    _l_(22297)

    self.assertEqual(x[i], tf_y[tf_idx[i]])
    _l_(22296)
