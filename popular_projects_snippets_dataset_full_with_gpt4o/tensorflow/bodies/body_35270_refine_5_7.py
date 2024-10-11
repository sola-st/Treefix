import unittest # pragma: no cover

class TestMock(unittest.TestCase): # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        with tf.Session() as sess: # pragma: no cover
            return sess.run(tensor) # pragma: no cover
self = TestMock() # pragma: no cover

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
