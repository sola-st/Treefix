import unittest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = type('Mock', (object,), {'assertRaisesOpError': Mock(), 'evaluate': Mock()})() # pragma: no cover

import unittest # pragma: no cover

class MyTest(unittest.TestCase):# pragma: no cover
    def assertRaisesOpError(self, msg):# pragma: no cover
        return self.assertRaisesRegex(tf.errors.CancelledError, msg)# pragma: no cover
# pragma: no cover
    def evaluate(self, op):# pragma: no cover
        with tf.compat.v1.Session() as sess:# pragma: no cover
            return sess.run(op)# pragma: no cover
# pragma: no cover
self = MyTest() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
