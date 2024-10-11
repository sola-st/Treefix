import unittest # pragma: no cover

class TestTakeOp(unittest.TestCase): # pragma: no cover
    def setUp(self): # pragma: no cover
        pass
    def assertRaisesOpError(self, message): # pragma: no cover
        return self.assertRaises(tf.OpError, self.takeg_op) # pragma: no cover
test_case = TestTakeOp() # pragma: no cover
test_case.setUp() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(5437)

    self.evaluate(takeg_op)
    _l_(5436)
