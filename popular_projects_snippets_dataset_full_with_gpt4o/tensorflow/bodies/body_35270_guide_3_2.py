class MockTestCase: # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        return tf.test.TestCase.assertRaisesWithPredicateMatch(self, tf.errors.InvalidArgumentError, lambda e: msg in str(e)) # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        if tf.executing_eagerly(): # pragma: no cover
            return tensor.numpy() # pragma: no cover
        else: # pragma: no cover
            with tf.compat.v1.Session() as sess: # pragma: no cover
                return sess.run(tensor) # pragma: no cover
self = type('Mock', (MockTestCase,), {})() # pragma: no cover

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
