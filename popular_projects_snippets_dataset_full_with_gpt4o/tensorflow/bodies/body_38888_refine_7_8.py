import unittest # pragma: no cover

self = type('Mock', (unittest.TestCase,), {'assertRaisesOpError': lambda self, message: self.assertRaises(tf.errors.OpError), 'evaluate': lambda self, op: tf.identity(op)})() # pragma: no cover

import unittest # pragma: no cover

Mock = type('Mock', (unittest.TestCase,), { 'assertRaisesOpError': lambda self, expected_message: self.assertRaises(tf.errors.CancelledError, msg=expected_message), 'evaluate': lambda self, op: (_ for _ in ()).throw(tf.errors.CancelledError(None, None, 'was cancelled'))}) # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
