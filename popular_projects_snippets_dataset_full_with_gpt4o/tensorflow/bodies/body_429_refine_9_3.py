import numpy as np # pragma: no cover

import unittest # pragma: no cover

class MockTest(unittest.TestCase):# pragma: no cover
    def cached_session(self):# pragma: no cover
        return tf.compat.v1.Session()# pragma: no cover
# pragma: no cover
mock_self = MockTest()# pragma: no cover
self = type('Mock', (object,), {'cached_session': mock_self.cached_session, 'assertEqual': mock_self.assertEqual})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v1_12.py
from l3.Runtime import _l_
sp_input = tf.SparseTensor(
    indices=tf.constant([[0, 1]], dtype=tf.int64),
    values=tf.constant([2], dtype=tf.int64),
    dense_shape=[1, 2])
_l_(19358)

with self.cached_session():
    _l_(19361)

    serialized_sp = tf.serialize_many_sparse(
        sp_input, 'serialize_name', tf.string)
    _l_(19359)
    self.assertEqual((1, 3), serialized_sp.shape)
    _l_(19360)
