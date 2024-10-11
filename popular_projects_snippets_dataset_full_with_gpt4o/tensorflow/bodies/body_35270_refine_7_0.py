import unittest # pragma: no cover

class MockTestCase(unittest.TestCase): # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        return self.assertRaisesRegex(tf.errors.InvalidArgumentError, msg) # pragma: no cover
    def evaluate(self, x): # pragma: no cover
        if tf.executing_eagerly(): # pragma: no cover
            return x.numpy() # pragma: no cover
        else: # pragma: no cover
            with tf.Session() as sess: # pragma: no cover
                return sess.run(x) # pragma: no cover
self = MockTestCase() # pragma: no cover

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
