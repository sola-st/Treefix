self = type('Mock', (object,), {'assertRaisesOpError': lambda self, msg: tf.errors.OpError(node_def=None, op=None, message=msg), 'evaluate': lambda self, op: op})() # pragma: no cover

import unittest # pragma: no cover

self = type('Mock', (unittest.TestCase,), {'assertRaisesOpError': lambda self, message: self.assertRaisesRegex(tf.errors.CancelledError, message), 'evaluate': lambda self, op: tf.constant(42)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
