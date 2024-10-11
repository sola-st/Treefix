class MockTestCase: # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        return tf.test.TestCase.assertRaisesWithPredicateMatch(self, tf.errors.InvalidArgumentError, lambda e: msg in str(e)) # pragma: no cover
    @staticmethod # pragma: no cover
    def evaluate(tensor): # pragma: no cover
        return tensor.numpy() if tf.executing_eagerly() else tf.get_static_value(tensor) # pragma: no cover
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
