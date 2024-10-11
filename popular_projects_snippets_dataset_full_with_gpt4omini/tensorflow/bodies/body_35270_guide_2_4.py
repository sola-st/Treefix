class MockTestCase:  # pragma: no cover
    def assertRaisesOpError(self, error_message): # pragma: no cover
        class ContextManager:  # pragma: no cover
            def __enter__(self):  # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                return isinstance(exc_value, tf.errors.InvalidArgumentError) # pragma: no cover
        return ContextManager() # pragma: no cover
    def evaluate(self, value):  # pragma: no cover
        return value # pragma: no cover
self = MockTestCase() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("Condition x > 0 did not hold"):
    _l_(6518)

    normal = normal_lib.Normal(
        loc=[1.], scale=[-5.], validate_args=True, name="G")
    _l_(6516)
    self.evaluate(normal.mean())
    _l_(6517)
