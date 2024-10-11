import unittest # pragma: no cover

self = type('Mock', (object,), {'assertRaisesOpError': lambda self, msg: unittest.TestCase().assertRaisesRegex(tf.errors.InvalidArgumentError, msg), 'evaluate': lambda self, tensor: tf.Session().run(tensor)})() # pragma: no cover

import unittest # pragma: no cover

class MockTest(unittest.TestCase): # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        return self.assertRaisesRegex(tf.errors.InvalidArgumentError, msg) # pragma: no cover
 # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        with tf.compat.v1.Session() as sess:  # tf.Session() is deprecated in tf v2.x # pragma: no cover
            return sess.run(tensor) # pragma: no cover
 # pragma: no cover
self = MockTest() # pragma: no cover

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
