import unittest # pragma: no cover

self = type('MockTestCase', (unittest.TestCase,), {})() # pragma: no cover
self.assertRaisesOpError = lambda expected_message: self.assertRaisesRegex(tf.errors.OpError, expected_message) # pragma: no cover
self.evaluate = lambda x: (_ for _ in ()).throw(tf.errors.CancelledError(None, None, 'was cancelled')) # pragma: no cover
takeg_op = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
