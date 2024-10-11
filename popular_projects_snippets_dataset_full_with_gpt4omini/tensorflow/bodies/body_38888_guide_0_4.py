import unittest # pragma: no cover

class MockOpError(Exception): pass # pragma: no cover
class TestTakegOp(unittest.TestCase): # pragma: no cover
    def setUp(self): # pragma: no cover
        pass
    def test_takeg_op_cancelled(self): # pragma: no cover
        with self.assertRaises(MockOpError): # pragma: no cover
            raise MockOpError('was cancelled') # pragma: no cover
if __name__ == '__main__': unittest.main() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(5437)

    self.evaluate(takeg_op)
    _l_(5436)
