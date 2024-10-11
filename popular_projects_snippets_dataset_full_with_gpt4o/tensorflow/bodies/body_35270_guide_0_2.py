import unittest # pragma: no cover

class MockTestCase(unittest.TestCase): # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        return tensor.numpy() # pragma: no cover
 # pragma: no cover
self = MockTestCase('__init__') # pragma: no cover
self.setUp() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("Condition x > 0 did not hold"):
    _l_(18549)

    normal = normal_lib.Normal(
        loc=[1.], scale=[-5.], validate_args=True, name="G")
    _l_(18547)
    self.evaluate(normal.mean())
    _l_(18548)
