class MockSelf: # pragma: no cover
    def assertRaisesOpError(*args, **kwargs): # pragma: no cover
        return tf.test.TestCase().__enter__() # pragma: no cover
    def evaluate(self, value): # pragma: no cover
        return tf.keras.backend.get_value(value) # pragma: no cover
self = MockSelf() # pragma: no cover

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
