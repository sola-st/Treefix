import numpy as np # pragma: no cover
import unittest # pragma: no cover

import unittest # pragma: no cover

self = type('Mock', (unittest.TestCase,), {'session': lambda self: tf.compat.v1.Session, 'assertRaises': unittest.TestCase.assertRaises, 'assertIn': unittest.TestCase.assertIn})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
from l3.Runtime import _l_
size_splits = array_ops.placeholder(dtype=dtypes.int32, shape=[None])
_l_(15844)

value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(15845)

with self.session() as sess:
    _l_(15849)

    with self.assertRaises(ValueError) as context:
        _l_(15847)

        sess.run(array_ops.split(value, size_splits), {size_splits: [2, 2, 6]})
        _l_(15846)
    self.assertIn("Cannot infer argument `num` from shape",
                  str(context.exception))
    _l_(15848)
