import unittest # pragma: no cover

class MockTestCase(unittest.TestCase): # pragma: no cover
    def assertRaisesOpError(self, expected_message): # pragma: no cover
        return self.assertRaisesRegex(tf.errors.OpError, expected_message) # pragma: no cover
 # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        return tf.convert_to_tensor(tensor) # pragma: no cover
 # pragma: no cover
self = MockTestCase() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
