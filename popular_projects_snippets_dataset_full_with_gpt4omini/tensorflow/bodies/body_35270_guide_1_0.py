class MockTestCase:  # pragma: no cover
    def assertRaisesOpError(self, message): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                if exc_type == tf.errors.InvalidArgumentError: # pragma: no cover
                    return True # pragma: no cover
                return False # pragma: no cover
        return ContextManager() # pragma: no cover
    def evaluate(self, value): return value # pragma: no cover
self = MockTestCase() # pragma: no cover
normal_lib = type('MockNormalLib', (object,), {})() # pragma: no cover

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
