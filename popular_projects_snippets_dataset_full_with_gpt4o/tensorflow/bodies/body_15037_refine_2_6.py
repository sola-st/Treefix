self = type('Mock', (object,), { # pragma: no cover
    'assertEqual': lambda x, y, z: x == z, # pragma: no cover
    'assertIs': lambda a, b, c: a is c, # pragma: no cover
    'assertAllEqual': lambda a, b, c: tf.reduce_all(tf.equal(a, b)), # pragma: no cover
    'assertAllEqual': lambda a, b, c: tf.reduce_all(tf.equal(a, c)) # pragma: no cover
})() # pragma: no cover

import unittest # pragma: no cover

self = type('Mock', (unittest.TestCase,), { # pragma: no cover
    'assertEqual': lambda self, a, b: self.assertTrue(a == b), # pragma: no cover
    'assertIs': lambda self, a, b: self.assertTrue(a is b), # pragma: no cover
    'assertAllEqual': lambda self, a, b: self.assertTrue((a == b).numpy().all()) # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
from l3.Runtime import _l_
values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
_l_(21950)
row_starts = constant_op.constant([0, 2, 2, 5, 6], dtypes.int64)
_l_(21951)

rt = RaggedTensor.from_row_starts(values, row_starts, validate=False)
_l_(21952)
self.assertEqual(rt.dtype, dtypes.string)
_l_(21953)
self.assertEqual(rt.shape.as_list(), [5, None])
_l_(21954)
self.assertEqual(rt.ragged_rank, 1)
_l_(21955)

rt_values = rt.values
_l_(21956)
rt_row_starts = rt.row_starts()
_l_(21957)
rt_nrows = rt.nrows()
_l_(21958)

self.assertIs(rt_values, values)
_l_(21959)
self.assertAllEqual(rt_nrows, 5)
_l_(21960)
self.assertAllEqual(rt_row_starts, row_starts)
_l_(21961)
self.assertAllEqual(rt,
                    [[b'a', b'b'], [], [b'c', b'd', b'e'], [b'f'], [b'g']])
_l_(21962)
