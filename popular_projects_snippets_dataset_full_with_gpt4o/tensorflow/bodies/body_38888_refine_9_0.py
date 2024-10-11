self = type('Mock', (object,), {'assertRaisesOpError': lambda self, msg: tf.errors.OpError(node_def=None, op=None, message=msg), 'evaluate': lambda self, op: op})() # pragma: no cover

import unittest # pragma: no cover

MockTestCase = type('MockTestCase', (unittest.TestCase,), {}) # pragma: no cover
self = MockTestCase() # pragma: no cover
self.assertRaisesOpError = lambda msg: self.assertRaisesRegex(tf.errors.CancelledError, msg) # pragma: no cover
self.evaluate = lambda op: (_ for _ in ()).throw(tf.errors.CancelledError(None, None, 'was cancelled')) # pragma: no cover
takeg_op = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
